import sys
from PyQt4 import QtCore, QtGui, uic
qtCreatorFile = "./mainwindow.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class myWidget(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)

def b1_clicked():
   print "Button 1 clicked"

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = myWidget()
	window.show()
	sys.exit(app.exec_())
