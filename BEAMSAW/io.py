#!/usr/bin/python
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse
from pprint import pprint
import time
import linuxcnc, hal

client= ModbusClient(method = "ascii", port="/dev/ttyUSB0", stopbits = 1, bytesize = 7, parity = 'E', baudrate= 9600)
connection = client.connect()
try:
	time.sleep(10)
	plc.ready()
	while True:
		result= client.read_discrete_inputs(1024,16,unit= 1)
		print(result.bits)
		time.sleep(.200)
except KeyboardInterrupt:
	client.close()
