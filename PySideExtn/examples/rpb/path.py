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

        #CHANGING THE PROGRESSABR STYLE
        self.rpb.setBarStyle('Hybrid1')

        #CHANGING THE LINE COLOR AND WIDTH
        self.rpb.setLineWidth(3)
        self.rpb2.setLineWidth(8)

        #PATH WIDTH
        self.rpb.setPathWidth(15)
        self.rpb2.setPathWidth(2)

        #CHANGING THE PATH COLOR
        self.rpb.setPathColor((125, 255, 255))
        self.rpb2.setPathColor((0, 0, 0))
        
        #SETTING THE VALUE
        self.rpb.setValue(85)
        self.rpb2.setValue(85)


        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.rpb)
        self.layout.addWidget(self.rpb2)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())