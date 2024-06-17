import sys
from PySide6 import QtCore, QtWidgets, QtGui
#IMPORTING THE MODULE
from PySideExtn.RoundProgressBar import RoundProgressBar

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        
        #CLASS INSTANCE
        self.rpb = RoundProgressBar()
        self.rpb2 = RoundProgressBar()
        self.rpb3 = RoundProgressBar()

        #LINE WIDTH 
        self.rpb.setLineWidth(10)

        #LINE CAP
        self.rpb.setLineCap('RoundCap')
        self.rpb2.setLineCap('SquareCap')
        self.rpb3.setLineCap('RoundCap')

        #LINE STYLE
        self.rpb3.setLineStyle('DotLine')
        self.rpb2.setLineStyle('DashLine')
        
        #SETTING THE VALUE
        self.rpb.setValue(85)
        self.rpb2.setValue(85)
        self.rpb3.setValue(85)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.rpb)
        self.layout.addWidget(self.rpb2)
        self.layout.addWidget(self.rpb3)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())