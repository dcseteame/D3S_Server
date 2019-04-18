import json

SIMULATION = False

data = []
index = 0

for i in range(1,5):
    f = open("../Simulation/data" + str(i) + ".json", "r")
    tmp = f.read()
    data.append(json.loads(tmp))
    f.close()

def injectAccelData(json_data):
    global index
    if SIMULATION == False:
        return
    else:
        actData = data[index]
        #print(actData)
        tmp = actData["accelerationX"]
        json_data["accelerationX"] = tmp
        json_data["accelerationY"] = actData["accelerationY"]
        json_data["accelerationZ"] = actData["accelerationZ"]
        index = index + 1
        if index == 4:
            index = 0
