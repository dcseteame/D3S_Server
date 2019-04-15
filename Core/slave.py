import json
import requests
import matplotlib.pyplot as plt
import numpy as np
import threading
import time

window_size = 500

class Slave(threading.Thread):

    URI = ""
    UID = ""
    dataset = {}

    def run(self):
        while True:
            print("Hi, I am " + threading.currentThread().getName())
            self.pollForData()

            testx = np.array(self.dataset[0]["accelerationX"])
            print(testx)

            time.sleep(1)


    def __init__(self, __uri, __uid):
        threading.Thread.__init__(self)
        self.URI = __uri
        self.UID = __uid

    def pollForData(self):
        # poll for devices
        r = requests.get(self.URI + "/" + self.UID + "?projection=deviceProjection")
        self.dataset = json.loads(r.text)["measurementEntries"]
        
    
    def getQuakeIntegral(self, json_data):

        x = np.array(self.dataset["x"])
        y = np.array(self.dataset["y"])
        z = np.array(self.dataset["z"])
        # FIXME: merge several measurments

        xyz = abs(x) + abs(y) + abs(z)
        samplingrate = self.dataset["samplingrate"]

        window_size_seconds = window_size / 1000
        num_values_per_window = int(samplingrate * window_size_seconds) # 1/s * s = 1
        num_splits = int(xyz.size / num_values_per_window)
        splits = np.array_split(xyz, num_splits)

        mean_array = np.zeros(num_splits)   # initialize

        for i in range(0, num_splits):
            mean_array[i] = splits[i].mean()
        
        max_val = np.max(mean_array)
        factor = 1 / max_val
        mean_array = mean_array * factor

        integral = np.trapz(mean_array)

        return integral
        