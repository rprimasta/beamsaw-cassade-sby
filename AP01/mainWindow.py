import sys
import inspect
from PyQt4 import QtCore, QtGui, uic
qtCreatorFile = "./mainwindow.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class mainWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(mainWindow,self).__init__()
		uic.loadUi('./mainwindow.ui',self)
		#QtGui.QMainWindow.__init__(self)
		#Ui_MainWindow.__init__(self)
		self.setupUi(self)
		#QPushButton("pushButton_3")
		self.pushButton_3.clicked.connect(self.btn3_clicked)
		
	def btn3_clicked(self):
		print "Button 3 clicked"

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = mainWindow()
	for name, data in inspect.getmembers(window):
    		if name.startswith('__'):
        		continue
    		print('{} : {!r}'.format(name, data))
	#window.button.clicked.connect(window.b1_clicked)
	window.show()
	sys.exit(app.exec_())
