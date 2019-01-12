You can only control the aircon by using the same reference to the one ac controller created at the start of the program.
All modules who import it has access and the ability to control it.

### Control / main modules and functions
- main.py :
	This module contains the Flask server

### Utilities libraries and modules
- MQTT module:
	A simple wrapper library/module over the single ended pub and sub actions provided by the paho MQTT package.
- pi_controller module:
	Defines the AC controller and its methods, for us to set AC state.
- BME_control module:
	Module used to read values (temp, humidity) from the BME Sensor.


#### LEGEND:
- rp: raspberry pi
- ac: aircon
- bz: buzzer

#### So what is the use case scenario?
1. Manual mode (Use phone to turn on and off the air con remotely)
    - Rmb that this means that I would need to control the rasp pi remotely.
    - Use MQTT without any security for now.
        - The "server" on the pi subscribes to the MQTT broker's topic,
        - Listens to commands that will come in.

2. Auto mode
    1. Set a "I'm coming home" mode. So just click on this mode before coming home, it will check temp and cool if needed
    2. "Always auto mode" that will constantly monitor the temp and cool hse if needed
        - This method means that the rp will be checking the temp every few seconds or mins
        - ?	determine if the temperature is too high
        - On ac
        - : off ac if it was on.
    3. Set a "timezone" thing, so that the auto mode is only activated when it is in the current time now.