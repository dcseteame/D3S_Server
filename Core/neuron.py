import threading
import time
import numpy as np

class Neuron(threading.Thread):
    bias = 0
    weight = 0
    T = 100
    step = 0.01
    weight0 = False
    FireState = 0

    def __init__(self):
        threading.Thread.__init__(self)
        self.bias = 5
        self.weight = 0
        self.weight0 = self.weight
        self.FireState = False
    
    def run(self):
        while True:
            d_weight = -(1/self.T) * self.weight0 * np.exp(-(1/self.T * self.step))
            self.weight = self.weight + d_weight
            
            if self.weight < 0:
                self.weight = 0
                
            #if self.weight > 0:
            #    print(self.weight)

            if self.weight > self.bias:
                self.FireState = True
                print("FIRE")
            else:
                self.FireState = False
                
            time.sleep(self.step)

    
    def updateBias(self, num_reg_devices):
        self.bias = int(num_reg_devices * 0.5) # TODO
    
    def add(self, value):
        self.weight = self.weight + value
        self.weight0 = self.weight

    def getWeight(self):
        return self.weight

            
