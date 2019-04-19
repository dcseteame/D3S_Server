from neuron import Neuron
import time

x = Neuron()
x.start()

while x.FireState == False:
    x.add(1)
    time.sleep(1)
