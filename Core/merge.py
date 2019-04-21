import threading
import requests
import time
import numpy as np
from debug import dlog
from neuron import Neuron

currentTime = lambda: int(round(time.time() * 1000))

measEntries = []

class Entry:
    def __init__(self):
        self.Time = 0
        self.Weight = 0
        self.Long = 0
        self.Lat = 0

def addMeasurement(Weight, Time, coordLong, coordLat):
    #entry = (Time, Weight, coordLong, coordLat)
    entry = Entry()
    entry.Time = Time
    entry.Weight = Weight
    entry.Long = coordLong
    entry.Lat = coordLat
    measEntries.append(entry)

    dlog("Measurement added")

class Merge(threading.Thread):
    URI = ""

    def __init__(self, __uri):
        threading.Thread.__init__(self)
        self.URI = __uri
        self.n = Neuron()
        self.n.start()
    
    def run(self):
        while True:
            for entry in measEntries:
                self.n.add(entry.Weight)
            
            measEntries.clear()

            if self.n.FireState == True:
                print("EARTHQUAKE!!!")
                requests.get(self.URI + "/warning?description=Earthquake")
            else:
                requests.get(self.URI + "/warning?description=ok")

            # TODO: low pass filter the switch between both warnings

            time.sleep(0.1)
