import sys
from PySide6 import QtCore, QtWidgets, QtGui

from PySideExtn.SpiralProgressBar import SpiralProgressBar #IMPORT THE EXTENSION LIBRARY

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.hello = 'Spiral Progress Bar'
        
        self.spbMinMax = SpiralProgressBar()    #SPIRAL PROGRESSBAR OBJECT
        self.spbRange = SpiralProgressBar()     #SPIRAL PROGRESS BAR OBJECT

        #SPIRAL PROGRESS BAR spbMinMax : GREEN COLOR
        self.spbMinMax.setMinimumValue((0, 0, 0))    #SETTING THE MINIMUM VALUE
        self.spbMinMax.setMaximumValue((360, 360, 360))   #SETTING THE MAXIMUM VALUE 
        self.spbMinMax.setLineColor((QtGui.QColor(0, 255, 0), QtGui.QColor(0, 255, 0), QtGui.QColor(0, 255, 0)))  #GREEN COLOR
        self.spbMinMax.setValue((300, 350, 289))    #SET THE CURRENT VALUE
        
        #SPIRAL PROGRESS BAR spbRange :BLUE COLOR
        self.spbRange.setRange((0, 0, 0), (360, 360, 360))  #SETTING THE RANGE
        self.spbRange.setValue((300, 350, 289)) #SETTING CURRENT VALUE
        
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.spbMinMax)
        self.layout.addWidget(self.spbRange) 
        self.setLayout(self.layout)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())