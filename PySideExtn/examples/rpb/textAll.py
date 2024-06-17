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
        self.rpb.setRange(0, 360) 
        self.rpb2.setRange(0, 360)
        self.rpb3.setRange(0, 360)
        
        #CHANGING THE STYLE
        self.rpb.setBarStyle('Pizza')
        self.rpb2.setBarStyle('Hybrid2')

        #CHANGING THE TEXT TYPE : VALUE OR PERCENTAGE
        self.rpb.setTextFormat('Value')
        self.rpb2.setTextFormat('Percentage')

        #CHANGING THE TEXT SIZE
        self.rpb.setTextRatio(3)
        self.rpb2.setTextRatio(9)

        #CHANGING THE FONT
        self.rpb.setTextFont('Arial')
        self.rpb2.setTextFont('Times New Roman')

        #TEXT HIDDEN
        self.rpb3.enableText(False)
        
        #SETTING THE VALUE
        self.rpb.setValue(156)
        self.rpb2.setValue(156)

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