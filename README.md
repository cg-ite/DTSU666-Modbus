# Why this fork?
I have a Qcells Q.VOLT-P5T-X inverter that only supports Modbus RTU. I'm trying to get the real-time data from the DSTU666, since the inverter only sends consumption data every 5 minutes.

Steps:
- cmd line app for reading the consumption data.


# Chint DTSU666-Modbus
Chint DTSU666-Modbus 3P4W Multifunction Power Analyser with RS485 port Modbus-RTU for the domoticz plugin

Installation: <br>
cd ~/domoticz/plugins<br>
git clone https://github.com/elfabriceu/DTSU666-Modbus <br>

<br>
Used python modules: <br>
pyserial -> -https://pythonhosted.org/pyserial/ <br>
minimalmodbus -> http://minimalmodbus.readthedocs.io<br>
<br>
Restart your domoticz server.
<br>
<br>
Tested on domoticz version: 2021.1

