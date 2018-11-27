import linuxcnc
import thread
import time
import os
import hal
import hal_glib

s = linuxcnc.stat()
c = linuxcnc.command()

def get_handlers(halcomp,builder,useropts):
        return [manualProg(halcomp,builder, useropts)]

class manualProg:
        def __init__(self,halcomp,builder,useropts):
                #hal_glib.GPin(halcomp.newpin('hal_currF', hal.HAL_FLOAT, hal.HAL_OUT))
                self.halcomp = halcomp
                self.builder = builder
		self.sawThick = 4.0
		#self.builder.get_object("panelWidthSpin").set_active()
	
	def on_exec_pressed(self,gtkobj,data=None):
		
		header_ngc = open("/root/linuxcnc/configs/BEAMSAW/post/header.ngc",'r')
		header = header_ngc.read()
		header_ngc.close()
		
		width = self.builder.get_object("panelWidthSpin").get_value()
		heigh = self.builder.get_object("panelHeighSpin").get_value()
		cutterComp = self.sawThick/2
		retract = "G90G54G0X{h}".format(h=heigh-cutterComp)
		cut  = "M302 M311\r\nM312\r\nM309\n\rM305\n\rM307\n\r"
		if width>1800:
			cut  = cut + "M301"
		else:
			cut  = cut + "M300"			 		
		cut  = "M303 M311\r\nM312\r\nM309\n\rM305\n\rM307\n\r"
		
		cutSize = [0]*10
		cutSize[0] = self.builder.get_object("sizeSpin1").get_value()
		cutSize[1] = self.builder.get_object("sizeSpin2").get_value()
		cutSize[2] = self.builder.get_object("sizeSpin3").get_value()
		cutSize[3] = self.builder.get_object("sizeSpin4").get_value()
		cutSize[4] = self.builder.get_object("sizeSpin5").get_value()
		cutSize[5] = self.builder.get_object("sizeSpin6").get_value()
		cutSize[6] = self.builder.get_object("sizeSpin7").get_value()
		cutSize[7] = self.builder.get_object("sizeSpin8").get_value()
		cutSize[8] = self.builder.get_object("sizeSpin9").get_value()
		cutSize[9] = self.builder.get_object("sizeSpin10").get_value()
		cutQty = [0]*10
		cutQty[0] = self.builder.get_object("qtySpin1").get_value()
		cutQty[1] = self.builder.get_object("qtySpin2").get_value()
		cutQty[2] = self.builder.get_object("qtySpin3").get_value()
		cutQty[3] = self.builder.get_object("qtySpin4").get_value()
		cutQty[4] = self.builder.get_object("qtySpin5").get_value()
		cutQty[5] = self.builder.get_object("qtySpin6").get_value()
		cutQty[6] = self.builder.get_object("qtySpin7").get_value()
		cutQty[7] = self.builder.get_object("qtySpin8").get_value()
		cutQty[8] = self.builder.get_object("qtySpin9").get_value()
		cutQty[9] = self.builder.get_object("qtySpin10").get_value()

		
		print ("Exec pressed")
