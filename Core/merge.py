import threading
import requests
import time
import numpy as np
from debug import dlog

PARAM_detectionVariance = 2

currentTime = lambda: int(round(time.time() * 1000))

measEntries = []

class Entry:
    def __init__(self):
        self.Time = 0
        self.EqInt = 0
        self.Long = 0
        self.Lat = 0

def addMeasurement(EqInt, Time, coordLong, coordLat):
    #entry = (Time, EqInt, coordLong, coordLat)
    entry = Entry()
    entry.Time = Time
    entry.EqInt = EqInt
    entry.Long = coordLong
    entry.Lat = coordLat
    measEntries.append(entry)

    dlog("Measurement added: ")
    dlog("Time: " + str(Time))
    #print("Coordinates: " + str(coordLong) + " / " + str(coordLat))
    dlog("Intensity: " + str(EqInt))

class Merge(threading.Thread):
    URI = ""

    def __init__(self, __uri):
        threading.Thread.__init__(self)
        self.URI = __uri
    
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
                    print("test")



            # calculate variance of EqInt, Lat, Long of each element of entriesToProcess
            if len(entriesToProcess) >= minEntries:
                EqIntMean = 0
                for entry in entriesToProcess:
                    EqIntMean = EqIntMean + entry.EqInt
                EqIntMean = EqIntMean / len(entriesToProcess)

                EqIntVar = 0
                for entry in entriesToProcess:
                    print("entry.EqInt = " + str(entry.EqInt))
                    print("EqIntMean = " + str(EqIntMean))
                    EqIntVar = EqIntVar + np.sqrt(abs(entry.EqInt - EqIntMean))
                EqIntVar = EqIntVar / len(entriesToProcess)
                print("EqIntVar = " + str(EqIntVar))

                if EqIntVar < PARAM_detectionVariance:
                    # earthquake!
                    print("EARTHQUAKE!!!")
                    requests.get(self.URI + "/warnings?description=Earthquake")

                    # remove measurements that led to a warning
                    for entry in entriesToProcess:
                        measEntries.remove(entry)

            time.sleep(1)
