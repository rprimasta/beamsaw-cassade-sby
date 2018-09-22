import sys
import inspect
from PyQt4 import *
from PyQt4 import uic,QtGui
from PyQt4.QtGui import *
qtCreatorFile = "./mainwindow.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

def getClassMember(object):
	for name, data in inspect.getmembers(object):
    		if name.startswith('__'):
        		continue
    		print('{} : {!r}'.format(name, data))


class mainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(mainWindow,self).__init__()
		uic.loadUi('./mainwindow.ui',self)
		#QtGui.QMainWindow.__init__(self)
		#Ui_MainWindow.__init__(self)
		self.setupUi(self)
		#QPushButton("pushButton_3")
		self.pushButton_3.clicked.connect(self.btn3_clicked)
		self.pushButton_4.clicked.connect(self.btn4_clicked)
		self.pushButton_5.clicked.connect(self.btn5_clicked)	
		self.pushButton_19.clicked.connect(self.btn19_clicked)	
		self.horizontalSlider_2.valueChanged.connect(self.feed_slider_moved)
	def feed_slider_moved(self,pos):
		self.label_19.setText('F : 5400(%d)' % pos)
	def btn19_clicked(self):
		w = QWidget()
		w.resize(320, 240)
		w.setWindowTitle("OPEN NC PROGRAM")
		filename = QFileDialog.getOpenFileName(w, 'Open File', '/')
		print filename
	def btn3_clicked(self):
		print "Button 3 clicked"
		getClassMember(self.horizontalSlider_2)
	def btn4_clicked(self):
		self.stackedWidget.setCurrentIndex(1)
	def btn5_clicked(self):
		self.stackedWidget.setCurrentIndex(0)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = mainWindow()
	#window.button.clicked.connect(window.b1_clicked)
	window.show()
	sys.exit(app.exec_())
