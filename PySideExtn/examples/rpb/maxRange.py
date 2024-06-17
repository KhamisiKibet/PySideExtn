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
        self.rpb3 = RoundProgressBar()

        #SETTING THE RANGE : MIN-0 & MAX:360
        self.rpb.setMaximum(720)
        self.rpb2.setRange(0, 720)
        self.rpb3.setRange(0, 1000)
        
        #SETTING THE VALUE
        self.rpb.setValue(456)
        self.rpb2.setValue(456)
        self.rpb3.setValue(890)

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