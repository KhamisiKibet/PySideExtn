import sys
from PySide6 import QtCore, QtWidgets, QtGui

from PySideExtn.SpiralProgressBar import SpiralProgressBar #IMPORT THE EXTENSION LIBRARY

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.hello = 'Spiral Progress Bar'
        
        self.spbN = SpiralProgressBar()    #SPIRAL PROGRESSBAR OBJECT

        self.spbN.setLineWidth(15)
        
        #VARIABLE WIDTH AND WIDTH INCREMENT
        self.spbN.variableWidth(True)
        self.spbN.widthIncrement(5)

        self.spbN.setValue((55, 55, 55))

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.spbN)
        self.setLayout(self.layout)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())