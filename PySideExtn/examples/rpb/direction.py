import sys
from PySide2 import QtCore, QtWidgets, QtGui
#IMPORTING THE MODULE
from PySideExtn.RoundProgressBar import RoundProgressBar

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        
        #CLASS INSTANCE
        self.rpb = RoundProgressBar()
        self.rpb2 = RoundProgressBar()
        
        #CHANGING THE DIRECTION
        self.rpb.setDirection('Clockwise')
        self.rpb2.setDirection('AntiClockwise')
        
        #SETTING THE VALUE
        self.rpb.setValue(56)
        self.rpb2.setValue(88)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.rpb)
        self.layout.addWidget(self.rpb2)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
        sys.exit(app.exec_())