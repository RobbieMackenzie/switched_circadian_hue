from qhue import Bridge
from time import sleep
from datetime import datetime as dt

with open("username.txt", "r") as f:
    username = f.read()
with open("bridge_ip_address.txt", "r") as f:
    bridge_ip = f.read()

bridge = Bridge(bridge_ip, username)

time = dt.utcnow()
checklight = bridge.lights[2]
lights_on = checklight()["state"]["on"]

button = bridge.sensors[2]
while 1 < 2:
    button_last_pressed = dt.fromisoformat(button()["state"]["lastupdated"])
    if button_last_pressed > time:
        print("Button pressed")
        time = dt.utcnow()
        if lights_on == False:
            print("light turning on")
            checklight.state(on=True)
            lights_on = True
        else:
            print("lights turning off")
            checklight.state(on=False)
            lights_on = False
    sleep(1)
            
            