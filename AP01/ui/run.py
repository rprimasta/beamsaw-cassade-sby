import linuxcnc
import hal
s = linuxcnc.stat()
c = linuxcnc.command()
#h = hal.component("../../BEAMSAW/BEAMSAW.hal")

def on_reset_press(gtkobj,data=None):
	for x in range(0,32):
		c.set_digital_output(x,0)
	c.reset_interpreter()
	print("Reset done.")
def saw_jog_pos_press(gtkobj,data=None):
	c.set_digital_output(13,1)
def saw_jog_pos_release(gtkobj,data=None):
	c.set_digital_output(13,0)
def saw_jog_neg_press(gtkobj,data=None):
	c.set_digital_output(14,1)
def saw_jog_neg_release(gtkobj,data=None):
	c.set_digital_output(14,0)

