#!/usr/bin/python
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse
from pprint import pprint
import time
import linuxcnc, hal

plc01 = hal.component("plc01")
plc01.newpin("x0", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("x1", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("x2", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("x3", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("x4", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("x5", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("x6", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("x7", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("x10", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("x11", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("x12", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("x13", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("x14", hal.HAL_BIT,hal.HAL_OUT) #AIR ALARM NC
plc01.newpin("x15", hal.HAL_BIT,hal.HAL_OUT) 
plc01.newpin("x16", hal.HAL_BIT,hal.HAL_OUT) 
plc01.newpin("x17", hal.HAL_BIT,hal.HAL_OUT) #EMERGENCY

plc01.newpin("y0", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y1", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y2", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y3", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y4", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y5", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y6", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y7", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y10", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y11", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y12", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y13", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y14", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y15", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y16", hal.HAL_BIT,hal.HAL_OUT)
plc01.newpin("y17", hal.HAL_BIT,hal.HAL_OUT)

plc01.newpin("M100", hal.HAL_BIT,hal.HAL_IN) #MACHINE ON
plc01.newpin("M101", hal.HAL_BIT,hal.HAL_IN) #SAW ON
plc01.newpin("M102", hal.HAL_BIT,hal.HAL_IN) #RESERVED
plc01.newpin("M103", hal.HAL_BIT,hal.HAL_IN) #RUN SAW01
plc01.newpin("M104", hal.HAL_BIT,hal.HAL_IN) #RUN SAW02
plc01.newpin("M105", hal.HAL_BIT,hal.HAL_IN) #RESERVED
plc01.newpin("M106", hal.HAL_BIT,hal.HAL_IN) #RESERVED
plc01.newpin("M107", hal.HAL_BIT,hal.HAL_IN) #RESERVED
plc01.newpin("M108", hal.HAL_BIT,hal.HAL_IN) #RESERVED
plc01.newpin("M109", hal.HAL_BIT,hal.HAL_IN) #RESERVED
plc01.newpin("M110", hal.HAL_BIT,hal.HAL_IN) #RESERVED
plc01.newpin("M111", hal.HAL_BIT,hal.HAL_IN) #RESERVED
plc01.newpin("M112", hal.HAL_BIT,hal.HAL_IN) #RESERVED
plc01.newpin("M113", hal.HAL_BIT,hal.HAL_IN) #RESERVED
plc01.newpin("M114", hal.HAL_BIT,hal.HAL_IN) #RESERVED
plc01.newpin("M115", hal.HAL_BIT,hal.HAL_IN) #RESERVED
plc01.newpin("M116", hal.HAL_BIT,hal.HAL_IN) #RESERVED

plc01.newpin("M512", hal.HAL_BIT,hal.HAL_OUT) #NORMAL STATE 
plc01.newpin("M513", hal.HAL_BIT,hal.HAL_OUT) #BUSY 
plc01.newpin("M514", hal.HAL_BIT,hal.HAL_OUT) #RESERVED 
plc01.newpin("M515", hal.HAL_BIT,hal.HAL_OUT) #RESERVED 
plc01.newpin("M516", hal.HAL_BIT,hal.HAL_OUT) #RESERVED 
plc01.newpin("M517", hal.HAL_BIT,hal.HAL_OUT) #RESERVED 
plc01.newpin("M518", hal.HAL_BIT,hal.HAL_OUT) #RESERVED 
plc01.newpin("M519", hal.HAL_BIT,hal.HAL_OUT) #RESERVED 


client= ModbusClient(method = "ascii", port="/dev/ttyUSB0", stopbits = 1, bytesize = 7, parity = 'E', baudrate= 9600)
connection = client.connect()

pinout = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

try:
	time.sleep(2)
	plc01.ready()
	while True:
		result= client.read_discrete_inputs(1024,16,unit= 1)
		for x in range(0, 16):
			if x<8:
				plc01['x' + str(x)] = result.bits[x]
			else: 		
				plc01['x' + str(x + 2)] = result.bits[x]
		result= client.read_coils(1280,16,unit= 1)
		for x in range(0, 16):
			if x<8:
				plc01['y' + str(x)] = result.bits[x]
			else: 		
				plc01['y' + str(x + 2)] = result.bits[x]

		result= client.read_coils(2560,16,unit= 1)
		for x in range(0, 8):
			plc01['M' + str(512 + x)] = result.bits[x]

		for x in range(0, 16):
			pinout[x] = plc01['M' + str(100 + x)]
		client.write_coils(2148,pinout,unit=1)

		time.sleep(.025)
		#print(result.bits)

except KeyboardInterrupt:
	client.close()
