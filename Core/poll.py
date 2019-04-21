import requests
import json
import threading
import time
from slave import Slave
import neuron

class Poll(threading.Thread):

    devListAct = []
    deviceMap = {}
    URI = ""
    
    def __init__(self, __uri):
        threading.Thread.__init__(self)
        self.URI = __uri

    def run(self):
        while True:
            # poll for devices
            r = requests.get(self.URI)
            json_data = r.text

            #f = open("devices.json", "r")
            #json_data = f.read()
            #f.close()

            deviceList_json = json.loads(json_data)["_embedded"]["devices"]

            devListNew = []
            for deviceEntry in deviceList_json:
                entry = (deviceEntry["id"], deviceEntry["samplingRate"], deviceEntry["longitude"], deviceEntry["latitude"])
                devListNew.append(entry)
            
            for device in devListNew:
                if device not in self.devListAct:
                    self.devListAct.append( device )
                    newSlave = Slave(self.URI, device[0], device[1])
                    self.deviceMap[device[0]] = newSlave
                    neuron.updateBias(len(self.devListAct))
                    newSlave.start()
                    # create new slave
            
            for device in self.devListAct:
                if  device not in devListNew:
                    removedDevice = self.deviceMap[device[0]]
                    removedDevice.stop()
                    self.devListAct.remove(device)
                    neuron.updateBias(len(self.devListAct))
                    # shut down slave
            
            #print(self.devListAct)
            
            time.sleep(1)
