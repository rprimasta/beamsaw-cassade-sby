import sys
import inspect
from PyQt4 import *
from PyQt4 import uic,QtGui
from PyQt4.QtGui import *

qtDialog_ui = "./ui/adv_start.ui"

Ui_Window, QtBaseClass = uic.loadUiType(qtDialog_ui)

class advStartWindow(QtGui.QDialog, Ui_Window):
	def __init__(self,initValue = 0):
		super(advStartWindow,self).__init__()
		self.setupUi(self)
		self.spinBox.setMaximum(999999999)
		self.spinBox.setValue(initValue)
		self.buttonBox.accepted.connect(self.ok_clicked)
		self.buttonBox.rejected.connect(self.cancel_clicked)
	def ok_clicked(self):
		self.lineNumber = self.spinBox.value()
		print self.lineNumber
		self.applied = True
		self.close()
	def cancel_clicked(self):
		self.applied = False
		self.close()
	def getValue(self):
		return self.lineNumber
	def getApplied(self):
                return self.applied
