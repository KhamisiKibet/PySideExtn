import sys
from PySide2 import QtCore, QtWidgets, QtGui

from PySideExtn.SpiralProgressBar import SpiralProgressBar #IMPORT THE EXTENSION LIBRARY

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.hello = 'Spiral Progress Bar'
        
        self.spbN = SpiralProgressBar()    #SPIRAL PROGRESSBAR OBJECT
        self.spbN.setNoProgressBar(4)
        
        #LINE WIDTH: 15px
        self.spbN.lineWidth(15)
        self.spbN.setGap(17)

        #LINE COLOR
        self.spbN.lineColor(((0, 125, 125), (125, 0, 125), (125, 255, 0), (125, 125, 125)))

        #LINE STYLE
        self.spbN.lineStyle(('SolidLine', 'DotLine', 'DashLine', 'SolidLine'))

        #LINE CAP
        self.spbN.lineCap(('SquareCap', 'RoundCap', 'RoundCap', 'SquareCap'))

        self.spbN.setValue((55, 55, 55, 55))

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.spbN)
        self.setLayout(self.layout)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())