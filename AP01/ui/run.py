import linuxcnc
import thread
import time
import os
import hal
import hal_glib
#from gladevcp.persistence import IniFile

#h = hal.component("../../BEAMSAW/BEAMSAW.hal")


#halcomp.hal_hbar1.set(1000)
s = linuxcnc.stat()
c = linuxcnc.command()

def get_handlers(halcomp,builder,useropts):
	return [myCallback(halcomp,builder, useropts)]

class myCallback:
	
	def __init__(self,halcomp,builder,useropts):
		hal_glib.GPin(halcomp.newpin('hal_currF', hal.HAL_FLOAT, hal.HAL_OUT))
		self.halcomp = halcomp
		self.builder = builder
		thread.start_new_thread(self.timer1, ("Timer1",0.1,) )
	def timer1(self, threadName, delay):
 		count = 0
   		while True:
      			time.sleep(delay)
			s.poll()
			if s.enabled is True:
				if s.exec_state is linuxcnc.EXEC_DONE:
					self.builder.get_object("label6").set_text('Ready')
				elif s.exec_state is linuxcnc.EXEC_WAITING_FOR_MOTION:
					self.builder.get_object("label6").set_text('Busy on Motion')
				elif s.exec_state is linuxcnc.EXEC_WAITING_FOR_MOTION_QUEUE:
					self.builder.get_object("label6").set_text('Busy on Motion Queue')
				#elif s.exec_state is linuxcnc.EXEC_WAITING_FOR_PAUSE:
				#	self.builder.get_object("label6").set_text('Busy on Pause')
				elif s.exec_state is linuxcnc.EXEC_WAITING_FOR_MOTION_AND_IO:
					self.builder.get_object("label6").set_text('Busy on Motion and IO ')
				elif s.exec_state is linuxcnc.EXEC_WAITING_FOR_DELAY:
					self.builder.get_object("label6").set_text('Busy on Delay')
				elif s.exec_state is linuxcnc.EXEC_WAITING_FOR_SYSTEM_CMD:
					self.builder.get_object("label6").set_text('Busy on System Command')
				elif s.exec_state is linuxcnc.EXEC_ERROR:
					self.builder.get_object("label6").set_text('Error')
			else:
				self.builder.get_object("label6").set_text('Not Ready')
				
			#self.halcomp['hal_currF'] = s.axis[0]['velocity']
      			#print "%s: %s" % ( threadName, time.ctime(time.time()) )

	def on_reset_press(self,gtkobj,data=None):
		for x in range(0,32):
			c.set_digital_output(x,0)
		c.reset_interpreter()
		print("Reset done.")
	def saw_jog_pos_press(self,gtkobj,data=None):
		c.set_digital_output(13,1)
	def saw_jog_pos_release(self,gtkobj,data=None):
		c.set_digital_output(13,0)
	def saw_jog_neg_press(self,gtkobj,data=None):
		c.set_digital_output(14,1)
	def saw_jog_neg_release(self,gtkobj,data=None):
		c.set_digital_output(14,0)


