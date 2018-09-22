import sys
from PyQt4.QtGui import *
from src.mainWindow import mainWindow

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = mainWindow()
	w.show()
	sys.exit(app.exec_())
