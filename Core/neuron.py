import threading
import time
import numpy as np

class Neuron(threading.Thread):
    bias = 0
    weight = 0
    oneOverT = 5 # = -1/T
    weight0 = 0

    def __init__(self):
        threading.Thread.__init__(self)
        self.bias = 3
        self.weight = 0
    
    def run(self):
        while True:
            d_weight = -(oneOverT) * self.weight0 * np.exp(-(oneOverT * 0.01))
            self.weight = self.weight - d_weight
            time.sleep(10)

    
    def updateBias(self, num_reg_devices):
        self.bias = 3 # TODO
    
    def add(value):
        self.weight = self.weight + value
        self.weight0 = self.weight
    
    def getFireState(self):
        if self.weight > bias:
            return True
        else
            return False
            