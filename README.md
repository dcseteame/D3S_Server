# Distributed Disaster Detection System
## About

## How to set up a prototype D3S environment
#### Prerequisites
* maven
* python3
* python3-numpy

#### Run the backend
1. Check out D3S_Server repository.
2. In directory *Server* run: `mvn package` and after that `mvn spring-boot:run`.
3. After the spring boot server started, go to directory *Core* and run `python3 main.py`.

#### Run the app
1. Check out Smartphone-Sensing-Framework repository from `github.com/dcseteame/Smartphone-Sensing-Framework` and make sure to be in branch `D3S@SSF2.0_AndroidStudio_2019`.
2. In `ConfigApp.java` change `backendURL` to the IP address of the machine, where the backend runs.
3. Build and run the app on at least 2 smartphones.

#### Test the system
1. Place both smartphones side by side on a table and wait for both to connect and register to the server. By observing the debug output of the python application, the connected devices can be noticed. Alternatively all registered devices can be looked up at the web page of the spring boot server: `http://{IP}:35673/devices`.
2. Shake the table slightly. Both smartphones should now send data to the server. After a moment the python application should print out `EARTHQUAKE!` at the debug output.
3. Now take one smartphone and put it on another table.
4. Shake ONE of both tables. Make sure the other table doesn't get affected.
5. The system should not report any earthquakes.

