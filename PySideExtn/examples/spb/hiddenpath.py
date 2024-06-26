import sys
from PySide6 import QtCore, QtWidgets, QtGui

from PySideExtn.SpiralProgressBar import SpiralProgressBar #IMPORT THE EXTENSION LIBRARY

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.hello = 'Spiral Progress Bar'
        
        self.spbN = SpiralProgressBar()    #SPIRAL PROGRESSBAR OBJECT

        self.spbN.setLineWidth(15)

        self.spbN.setPathHidden(True)

        self.spbN.setValue((55, 15, 69))

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.spbN)
        self.setLayout(self.layout)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())