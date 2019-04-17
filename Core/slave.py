import json
import requests
import matplotlib.pyplot as plt
import numpy as np
import threading
import time
import merge
import simulationInjection as sI

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

                if i == 0:
                    sI.injectAccelData(measEntries[i])

                EqInt = self.getQuakeIntegral(measEntries[i])
                if EqInt > 0:
                    merge.addMeasurement(EqInt, self.dataset["measurementEntries"][i]["time"], self.dataset["longitude"], self.dataset["latitude"])
                    #print("New measurement: " + str(i) + " " + str(EqInt))

            self.datasetIdx = len(measEntries)

            #testx = np.array(self.dataset[0]["accelerationX"])
            #print(testx)

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
        
    
    def getQuakeIntegral(self, actDataset):

        if self.samplingrate == 0:
            return 0
        #self.samplingrate = 60.0 # fix due to smartphone sensing framework

        x = np.array(actDataset["accelerationX"])
        y = np.array(actDataset["accelerationY"])
        z = np.array(actDataset["accelerationZ"])

        if sum(x) == 0 and sum(y) == 0 and sum(z) == 0:
            return 0

        xyz = abs(x) + abs(y) + abs(z)

        window_size_seconds = window_size / 1000
        num_values_per_window = int(self.samplingrate * window_size_seconds) # 1/s * s = 1

        if num_values_per_window == 0:
            return 0

        num_splits = int(xyz.size / num_values_per_window)
        splits = np.array_split(xyz, num_splits)

        mean_array = np.zeros(num_splits)   # initialize

        for i in range(0, num_splits):
            mean_array[i] = splits[i].mean()
        
        max_val = np.max(mean_array)

        if max_val == 0:
            return 0

        factor = 1 / max_val
        mean_array = mean_array * factor

        integral = np.trapz(mean_array)

        return integral
        