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

    dlog("Measurement added: ")
    dlog("Time: " + str(Time))
    #print("Coordinates: " + str(coordLong) + " / " + str(coordLat))
    dlog("Intensity: " + str(Weight))

class Merge(threading.Thread):
    URI = ""

    def __init__(self, __uri):
        threading.Thread.__init__(self)
        self.URI = __uri
        self.n = Neuron()
        self.n.start()
    
    def run(self):
        while True:
            minEntries = 3  # TODO: set dynamically based on registered devices

            entriesToProcess = []
            for entry in measEntries:
                # XXX: ignore time for debug reasons
                #if (currentTime() - entry.Time) < 5000:
                if True:
                    entriesToProcess.append(entry)
                else:
                    measEntries.remove(entry)  # XXX: does it work?
            
            if len(entriesToProcess) > 0:
                for entry in entriesToProcess:
                    self.n.add(entry.Weight)
            
            if self.n.FireState == True:
                print("EARTHQUAKE!!!")
                requests.get(self.URI + "/warnings?description=Earthquake")

            time.sleep(1)

