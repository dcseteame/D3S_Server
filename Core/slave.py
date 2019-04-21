import json
import requests
import numpy as np
import threading
import time
import merge
import simulationInjection as sI
from debug import dlog

class Slave(threading.Thread):

    URI = ""
    UID = ""
    dataset = {}
    datasetIdx = 0
    samplingrate = 0

    stopsig = False

    def run(self):
        # ignore old data
        self.pollForData()
        measEntries = self.dataset["measurementEntries"]
        self.datasetIdx = len(measEntries)

        while True:
            #dlog("Hi, I am slave " + threading.currentThread().getName())
            if self.stopsig == True:
                print("Goodbye!")
                return
            
            self.pollForData()

            measEntries = self.dataset["measurementEntries"]

            for i in range(self.datasetIdx, len(measEntries)):
                #dlog("measurementEntry: " + str(i))

                try:
                    NormMean, Std = self.getMeanStd(measEntries[i])
                    dlog("%s: mean = %.2f, std = %.3f" % (threading.currentThread().name, NormMean, Std))

                    if Std > 0.015:
                        merge.addMeasurement(1, self.dataset["measurementEntries"][i]["time"], self.dataset["longitude"], self.dataset["latitude"])
                except:
                    print("evaluation error")

            self.datasetIdx = len(measEntries)
            time.sleep(1)

    def stop(self):
        self.stopsig = True

    def __init__(self, __uri, __uid, __samplingrate):
        threading.Thread.__init__(self)
        self.URI = __uri
        self.UID = __uid
        self.samplingrate = __samplingrate

    def pollForData(self):
        # poll for devices
        r = requests.get(self.URI + "/" + self.UID + "?projection=deviceProjection")
        try:
            self.dataset = json.loads(r.text)
        except:
            print(r.text)
    
    def getMeanStd(self, actDataset):
        if self.samplingrate == 0:
            return 0

        xdata = actDataset["accelerationX"]
        ydata = actDataset["accelerationY"]
        zdata = actDataset["accelerationZ"]

        if xdata == None or ydata == None or zdata == None:
            dlog("no valid data: None")
            return 0

        x = np.array(xdata)
        y = np.array(ydata)
        z = np.array(zdata)

        if sum(x) == 0 and sum(y) == 0 and sum(z) == 0:
            dlog("no valid data: 0")
            return 0

        xyz = abs(x) + abs(y) + abs(z)
        std = xyz.std()

        max_val = xyz.max()
        if max_val == 0:
            dlog("no valid data: max_val = 0")
            return 0
        
        factor = 1 / max_val
        xyz = xyz * factor  # normalize

        return xyz.mean(), std
