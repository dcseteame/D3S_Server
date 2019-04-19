import json
import requests
import numpy as np
import threading
import time
import merge
import simulationInjection as sI
from debug import dlog

window_size = 500 # milliseconds

class Slave(threading.Thread):

    URI = ""
    UID = ""
    dataset = {}
    datasetIdx = 0
    samplingrate = 0

    stopsig = False

    def run(self):
        while True:
            print("Hi, I am " + threading.currentThread().getName())
            if self.stopsig == True:
                print("Goodbye!")
                return
            
            self.pollForData()

            measEntries = self.dataset["measurementEntries"]

            for i in range(self.datasetIdx, len(measEntries)):
                dlog("measurementEntry: " + str(i))

                if i == 0:
                    sI.injectAccelData(measEntries[i])

                EqInt = self.getMeanValue(measEntries[i])
                if EqInt > 0:
                    merge.addMeasurement(EqInt, self.dataset["measurementEntries"][i]["time"], self.dataset["longitude"], self.dataset["latitude"])
                    dlog("New measurement: " + str(i) + " " + str(EqInt))

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
        self.dataset = json.loads(r.text)
    
    def getMeanValue(self, actDataset):
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
        return xyz.mean()
