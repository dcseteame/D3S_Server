import threading
import time
import numpy as np

bias = 999999
device_factor = 0.7
max_weight = lambda: (bias * 2)

def updateBias(num_reg_devices):
    global bias
    if num_reg_devices > 1:
        bias = num_reg_devices * device_factor # TODO
    else:
        bias = device_factor * 2
    print("New bias: " + str(bias))

class Neuron(threading.Thread):
    weight = 0
    step = 0.1
    T = 100*step
    weight0 = False
    FireState = 0

    def __init__(self):
        threading.Thread.__init__(self)
        self.weight = 0
        self.weight0 = self.weight
        self.FireState = False

    def run(self):
        global bias
        while True:
            d_weight = -(1/self.T) * self.weight0 * np.exp(-(1/self.T * self.step))
            self.weight = self.weight + d_weight
            
            if self.weight < 0:
                self.weight = 0
                
            #if self.weight > 0:
            #    print(self.weight)

            if self.weight > bias:
                self.FireState = True
                #print("FIRE")
            else:
                self.FireState = False
                
            time.sleep(self.step)

    def add(self, value):
        self.weight = self.weight + value
        self.weight0 = self.weight

    def getWeight(self):
        return self.weight

            
