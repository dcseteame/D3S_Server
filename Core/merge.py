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
    eqc = 0 # counter

    def __init__(self, __uri):
        threading.Thread.__init__(self)
        self.URI = __uri
        self.n = Neuron()
        self.n.start()
        self.eqc = 0
    
    def run(self):
        while True:
            for entry in measEntries:
                self.n.add(entry.Weight)
            
            measEntries.clear()

            if self.n.FireState == True:
                self.eqc = self.eqc + 1
                if self.eqc > 20:
                    self.eqc = 20
            else:
                if self.eqc > 0:
                    self.eqc = self.eqc - 1

            if self.eqc > 10:
                print("EARTHQUAKE!!!")
                requests.get(self.URI + "/warning?description=Earthquake")
            elif self.eqc < 5:
                requests.get(self.URI + "/warning?description=ok")

            time.sleep(0.1)
