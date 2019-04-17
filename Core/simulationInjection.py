SIMULATION = True

data = []
index = 0

for i in range(1,5):
    f = open("../Simulation/data" + str(i) + ".json", "r")
    tmp = f.read()
    data.append(tmp)
    f.close()

def injectAccelData(json_data):
    if SIMULATION == False:
        return
    else:
        json_data["accelerationX"] = data[index]["accelerationX"]
        json_data["accelerationY"] = data[index]["accelerationY"]
        json_data["accelerationZ"] = data[index]["accelerationZ"]
        json_data["samplingRate"] = data[index]["samplingRate"]
        index = index + 1
        if index == 4:
            index = 0
