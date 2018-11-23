#!/usr/bin/python
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse
from pprint import pprint
import time
import linuxcnc, hal

updateRate = 0.050 ##Second

plc = hal.component("plc01")
plc.newpin("in.x0", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x1", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x2", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x3", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x4", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x5", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x6", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x7", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x10", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x11", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x12", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x13", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x14", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x15", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x16", hal.HAL_BIT, hal.HAL_OUT)
plc.newpin("in.x17", hal.HAL_BIT, hal.HAL_OUT)


plc.newpin("out.y0", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y1", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y2", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y3", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y4", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y5", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y6", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y7", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y10", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y11", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y12", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y13", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y14", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y15", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y16", hal.HAL_BIT, hal.HAL_IN)
plc.newpin("out.y17", hal.HAL_BIT, hal.HAL_IN)

client= ModbusClient(method = "ascii", port="/dev/ttyUSB0", stopbits = 1, bytesize = 7, parity = 'E', baudrate= 9600)
connection = client.connect()
try:
	time.sleep(10)
	plc.ready()
	while True:
		result= client.read_discrete_inputs(1024,16,unit= 1)
		plc['in.x0'] = result.bits[0] 
		plc['in.x1'] = result.bits[1] 
		plc['in.x2'] = result.bits[2] 
		plc['in.x3'] = result.bits[3] 
		plc['in.x4'] = result.bits[4] 
		plc['in.x5'] = result.bits[5] 
		plc['in.x6'] = result.bits[6] 
		plc['in.x7'] = result.bits[7] 
		plc['in.x10'] = result.bits[8] 
		plc['in.x11'] = result.bits[9] 
		plc['in.x12'] = result.bits[10] 
		plc['in.x13'] = result.bits[11] 
		plc['in.x14'] = result.bits[12] 
		plc['in.x15'] = result.bits[13] 
		plc['in.x16'] = result.bits[14] 
		plc['in.x17'] = result.bits[15] 
		#print(result.bits)
		time.sleep(.200)
except KeyboardInterrupt:
	client.close()
