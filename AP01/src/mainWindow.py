import sys
from PyQt4 import *
from PyQt4 import uic,QtGui
from PyQt4.QtGui import *
from debug_tool import debug
from adv_start import advStartWindow
qtMainWindow_ui = "./ui/mainwindow.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtMainWindow_ui)
dbg = debug()


class mainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(mainWindow,self).__init__()
		self.setupUi(self)
		self.pushButton_3.clicked.connect(self.btn3_clicked)
		self.pushButton_4.clicked.connect(self.btn4_clicked)
		self.pushButton_5.clicked.connect(self.btn5_clicked)	
		self.pushButton_19.clicked.connect(self.btn19_clicked)	
		self.pushButton_20.clicked.connect(self.btn20_clicked)	
		self.horizontalSlider_2.valueChanged.connect(self.feed_slider_moved)
	def feed_slider_moved(self,pos):
		self.label_19.setText('F : 5400(%d)' % pos)
	def btn19_clicked(self):
		w = QWidget()
		w.resize(320, 240)
		w.setWindowTitle("OPEN NC PROGRAM")
		filename = QFileDialog.getOpenFileName(w, 'Open File', '/')
		print filename
	def btn20_clicked(self):
		w = advStartWindow(self.lcdNumber.intValue())
		#w.show()
		w.exec_()
		if w.getApplied() == True:
			self.lcdNumber.display(w.getValue())
	def btn3_clicked(self):
		print "Button 3 clicked"
		dbg.getClassMember(self.horizontalSlider_2)
	def btn4_clicked(self):
		self.stackedWidget.setCurrentIndex(1)
	def btn5_clicked(self):
		self.stackedWidget.setCurrentIndex(0)


