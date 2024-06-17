#############################################################################################
# CREATOR:  ANJAL.P                                                                         #
# ON:       2020 NOV.                                                                       #
# AIM:      To Extend the capability of the PySide2 and PyQt5 Python library with easy to   #
#           use extension containing commonly used widgets which is not natively supported  #
#           by the Qt Frame work (or atleast for Python version of Qt).                     #
# VERSION:  v1.0.0                                                                          #
# NOTES:    Demo Application 										                        #
# REFER:    Github: https://github.com/anjalp/PySideExtn                                   #
#############################################################################################


from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from PySideExtn.RoundProgressBar import RoundProgressBar
from PySideExtn.SpiralProgressBar import SpiralProgressBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 415)
        MainWindow.setMinimumSize(QSize(800, 415))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.b1 = QPushButton(self.widget)
        self.b1.setObjectName(u"b1")
        self.b1.setMinimumSize(QSize(20, 20))
        self.b1.setMaximumSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.b1, 0, 1, 1, 1)

        self.b3 = QPushButton(self.widget)
        self.b3.setObjectName(u"b3")
        self.b3.setMinimumSize(QSize(20, 20))
        self.b3.setMaximumSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.b3, 0, 5, 1, 1)

        self.rpb4 = RoundProgressBar(self.widget)
        self.rpb4.setObjectName(u"rpb4")

        self.gridLayout_2.addWidget(self.rpb4, 0, 6, 3, 1)

        self.rpb3 = RoundProgressBar(self.widget)
        self.rpb3.setObjectName(u"rpb3")

        self.gridLayout_2.addWidget(self.rpb3, 0, 4, 3, 1)

        self.rpb2 = RoundProgressBar(self.widget)
        self.rpb2.setObjectName(u"rpb2")
        self.rpb2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.rpb2, 0, 2, 3, 1)

        self.rpb1 = RoundProgressBar(self.widget)
        self.rpb1.setObjectName(u"rpb1")

        self.gridLayout_2.addWidget(self.rpb1, 0, 0, 3, 1)

        self.b2 = QPushButton(self.widget)
        self.b2.setObjectName(u"b2")
        self.b2.setMinimumSize(QSize(20, 20))
        self.b2.setMaximumSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.b2, 2, 1, 1, 1)

        self.vs1 = QSlider(self.widget)
        self.vs1.setObjectName(u"vs1")
        self.vs1.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.vs1, 0, 3, 3, 1)

        self.b4 = QPushButton(self.widget)
        self.b4.setObjectName(u"b4")
        self.b4.setMinimumSize(QSize(20, 20))
        self.b4.setMaximumSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.b4, 2, 5, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.hs1 = QSlider(self.tab)
        self.hs1.setObjectName(u"hs1")
        self.hs1.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.hs1)

        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.vs2 = QSlider(self.widget_2)
        self.vs2.setObjectName(u"vs2")
        self.vs2.setOrientation(Qt.Vertical)
        self.vs2.setInvertedAppearance(True)

        self.gridLayout_3.addWidget(self.vs2, 0, 3, 4, 1)

        self.b6 = QPushButton(self.widget_2)
        self.b6.setObjectName(u"b6")
        self.b6.setMinimumSize(QSize(20, 20))
        self.b6.setMaximumSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.b6, 3, 5, 1, 1)

        self.b5 = QPushButton(self.widget_2)
        self.b5.setObjectName(u"b5")
        self.b5.setMinimumSize(QSize(20, 20))
        self.b5.setMaximumSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.b5, 0, 5, 1, 1)

        self.b8 = QPushButton(self.widget_2)
        self.b8.setObjectName(u"b8")
        self.b8.setMinimumSize(QSize(20, 20))
        self.b8.setMaximumSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.b8, 3, 1, 1, 1)

        self.rpb5 = RoundProgressBar(self.widget_2)
        self.rpb5.setObjectName(u"rpb5")

        self.gridLayout_3.addWidget(self.rpb5, 0, 0, 4, 1)

        self.b7 = QPushButton(self.widget_2)
        self.b7.setObjectName(u"b7")
        self.b7.setMinimumSize(QSize(20, 20))
        self.b7.setMaximumSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.b7, 0, 1, 1, 1)

        self.rpb7 = RoundProgressBar(self.widget_2)
        self.rpb7.setObjectName(u"rpb7")

        self.gridLayout_3.addWidget(self.rpb7, 0, 4, 4, 1)

        self.rpb8 = RoundProgressBar(self.widget_2)
        self.rpb8.setObjectName(u"rpb8")

        self.gridLayout_3.addWidget(self.rpb8, 0, 6, 4, 1)

        self.rpb6 = RoundProgressBar(self.widget_2)
        self.rpb6.setObjectName(u"rpb6")

        self.gridLayout_3.addWidget(self.rpb6, 0, 2, 4, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.tab_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.widget_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(20, 20))
        self.pushButton_9.setMaximumSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_9, 0, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.widget_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(20, 20))
        self.pushButton_11.setMaximumSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_11, 0, 5, 1, 1)

        self.pushButton_10 = QPushButton(self.widget_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(20, 20))
        self.pushButton_10.setMaximumSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_10, 3, 1, 1, 1)

        self.vs3 = QSlider(self.widget_3)
        self.vs3.setObjectName(u"vs3")
        self.vs3.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.vs3, 0, 3, 4, 1)

        self.spb2 = SpiralProgressBar(self.widget_3)
        self.spb2.setObjectName(u"spb2")

        self.gridLayout_4.addWidget(self.spb2, 0, 2, 4, 1)

        self.spb1 = SpiralProgressBar(self.widget_3)
        self.spb1.setObjectName(u"spb1")

        self.gridLayout_4.addWidget(self.spb1, 0, 0, 4, 1)

        self.spb3 = SpiralProgressBar(self.widget_3)
        self.spb3.setObjectName(u"spb3")

        self.gridLayout_4.addWidget(self.spb3, 0, 4, 4, 1)

        self.pushButton_12 = QPushButton(self.widget_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(20, 20))
        self.pushButton_12.setMaximumSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_12, 3, 5, 1, 1)

        self.spb4 = SpiralProgressBar(self.widget_3)
        self.spb4.setObjectName(u"spb4")

        self.gridLayout_4.addWidget(self.spb4, 0, 6, 4, 1)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.hs2 = QSlider(self.tab_2)
        self.hs2.setObjectName(u"hs2")
        self.hs2.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.hs2)

        self.widget_4 = QWidget(self.tab_2)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_5 = QGridLayout(self.widget_4)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_15 = QPushButton(self.widget_4)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(20, 20))
        self.pushButton_15.setMaximumSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.pushButton_15, 0, 5, 1, 1)

        self.pushButton_13 = QPushButton(self.widget_4)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(20, 20))
        self.pushButton_13.setMaximumSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.pushButton_13, 0, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.widget_4)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(20, 20))
        self.pushButton_16.setMaximumSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.pushButton_16, 3, 5, 1, 1)

        self.pushButton_14 = QPushButton(self.widget_4)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(20, 20))
        self.pushButton_14.setMaximumSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.pushButton_14, 3, 1, 1, 1)

        self.spb5 = SpiralProgressBar(self.widget_4)
        self.spb5.setObjectName(u"spb5")

        self.gridLayout_5.addWidget(self.spb5, 0, 0, 4, 1)

        self.spb6 = SpiralProgressBar(self.widget_4)
        self.spb6.setObjectName(u"spb6")

        self.gridLayout_5.addWidget(self.spb6, 0, 2, 4, 1)

        self.spb7 = SpiralProgressBar(self.widget_4)
        self.spb7.setObjectName(u"spb7")

        self.gridLayout_5.addWidget(self.spb7, 0, 4, 4, 1)

        self.spb8 = SpiralProgressBar(self.widget_4)
        self.spb8.setObjectName(u"spb8")

        self.gridLayout_5.addWidget(self.spb8, 0, 6, 4, 1)

        self.vs4 = QSlider(self.widget_4)
        self.vs4.setObjectName(u"vs4")
        self.vs4.setOrientation(Qt.Vertical)
        self.vs4.setInvertedAppearance(True)

        self.gridLayout_5.addWidget(self.vs4, 0, 3, 4, 1)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Demo Application PySideExtn", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.b3.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.b2.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.b4.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.b6.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.b5.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.b8.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.b7.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"RoundProgressBar", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"SpiralProgressBar", None))

        self.addDesignTothis()
    

    def addDesignTothis(self):
        self.widget_rpb()
        self.widget_spb()


    def widget_rpb(self):

        self.rpb1.setValue(55)
        self.rpb2.setValue(84)
        self.rpb3.setValue(0)
        self.rpb4.setValue(46)
        self.rpb5.setValue(75)
        self.rpb6.setValue(66)
        self.rpb7.setValue(5)
        self.rpb8.setValue(95)


        self.rpb2.setBarStyle("Line")
        self.rpb2.setLineColor((0, 10, 15))
        self.rpb2.setTextColor((0, 10, 15))


        self.rpb3.setBarStyle("Pie")
        self.rpb3.setMaximum(360)
        self.rpb3.setTextFormat('Value')
        self.rpb3.setTextColor((210, 240, 210))
        self.rpb3.setPieColor((0, 125, 125))


        self.rpb4.setBarStyle("Pizza")
        self.rpb4.setRange(0, 200)
        self.rpb4.setCircleColor((210, 100, 0))
        self.rpb4.setLineColor((160, 50, 0))
        self.rpb4.setTextColor((250, 250, 250))
        self.rpb4.setCircleRatio(1)


        self.rpb5.setBarStyle("Hybrid1")
        self.rpb5.setRange(0, 360)
        self.rpb5.setTextFormat('Value')
        self.rpb5.setPathWidth(2)
        self.rpb5.setLineWidth(8)
        self.rpb5.setPathColor((100, 100, 100))
        self.rpb5.setCircleColor((100, 100, 100))
        self.rpb5.setTextColor((250, 250, 250))


        self.rpb6.setBarStyle("Hybrid2")


        self.rpb8.setBarStyle("Hybrid1")
        self.rpb8.setRange(0, 360)


        self.rpb7.setLineWidth(2)
        self.rpb7.setLineColor((20, 20, 20))
        self.rpb7.setMaximum(200)
        self.rpb7.enableText(False)
        self.rpb7.setPathWidth(8)

        self.hs1.valueChanged.connect(lambda: self.rpb1.setValue(self.hs1.value()))
        self.hs1.valueChanged.connect(lambda: self.rpb8.setValue(100 - self.hs1.value()))
        self.hs1.valueChanged.connect(lambda: self.rpb4.setValue(200 - self.hs1.value()))
        self.hs1.valueChanged.connect(lambda: self.rpb5.setValue(2*self.hs1.value()))

        self.vs1.valueChanged.connect(lambda: self.rpb2.setValue(self.vs1.value()))
        self.vs1.valueChanged.connect(lambda: self.rpb3.setValue(360 - self.vs1.value()))

        self.vs2.valueChanged.connect(lambda: self.rpb6.setValue(self.vs2.value()))
        self.vs2.valueChanged.connect(lambda: self.rpb7.setValue(self.vs2.value()))


        self.b1.clicked.connect(lambda: self.rpb1.setLineColor((128, 40, 152)))
        self.b2.clicked.connect(lambda: self.rpb8.setCircleColor((0, 192, 175)))
        self.b5.clicked.connect(lambda: self.rpb6.setTextColor((0, 192, 175)))
        self.b3.clicked.connect(lambda: self.rpb3.setValue(0))
        self.b4.clicked.connect(lambda: self.rpb3.setValue(100))
        self.b6.clicked.connect(lambda: self.rpb5.setValue(0))
        self.b7.clicked.connect(lambda: self.rpb6.setValue(100))
        self.b8.clicked.connect(lambda: self.rpb8.setValue(360))


    def widget_spb(self):

        self.spb1.setValue((82, 56, 5))

        self.spb2.setNoProgressBar(2)
        self.spb2.lineWidth(15)
        self.spb2.setGap(18)
        self.spb2.setValue((65, 60))
        self.spb2.lineColor(((28, 129, 196), (90, 193, 211)))
        self.spb2.pathColor(((195, 225, 242), (208, 234, 244)))

        self.spb3.setRange((0, 0, 0), (360, 360, 360))
        self.spb3.lineWidth(15)
        self.spb3.setGap(17)
        self.spb3.setInitialPos(('East', 'East', 'East'))
        self.spb3.setValue((246, 315, 198))
        self.spb3.setPathHidden(True)

        self.spb4.setNoProgressBar(6)
        self.spb4.lineWidth(10)
        self.spb4.setGap(11)
        self.spb4.setValue((59, 16, 27, 65, 84, 95))

        self.spb5.lineStyle(('DotLine', 'DotLine', 'DotLine'))
        self.spb5.setValue((65, 90, 25))

        self.spb6.setNoProgressBar(5)
        self.spb6.lineWidth(10)
        self.spb6.setGap(11)
        self.spb6.setDirection(('Clockwise', 'AntiClockwise', 'AntiClockwise', 'Clockwise', 'Clockwise'))
        self.spb6.setValue((65, 25, 86, 45, 75))
        
        self.spb7.setGap(12)
        self.spb7.variableWidth(True)
        self.spb7.widthIncrement(2)
        
        self.spb8.lineWidth(8)
        self.spb8.setGap(9)
        self.spb8.lineCap(('RoundCap', 'SquareCap', 'SquareCap'))
        self.spb8.setValue((65, 23, 95))

        self.hs2.valueChanged.connect(lambda: self.spb1.setValue((self.hs2.value(), self.hs2.value()*1.5, self.hs2.value()*1.75)))
        self.hs2.valueChanged.connect(lambda: self.spb4.setValue((self.hs2.value()*1.25, self.hs2.value()*1.35, self.hs2.value()*1, self.hs2.value()*1.75, self.hs2.value()*1.55, self.hs2.value()*0.45)))
        self.hs2.valueChanged.connect(lambda: self.spb5.setValue((360 - self.hs2.value()*3.6, 360 - self.hs2.value()*4, 360 - self.hs2.value()*4.2)))
        self.hs2.valueChanged.connect(lambda: self.spb8.setValue((self.hs2.value(), self.hs2.value()*1.26, self.hs2.value()*2)))

        self.vs3.valueChanged.connect(lambda: self.spb2.setValue((100 - self.vs3.value()*1.2, 100 - self.vs3.value())))
        self.vs3.valueChanged.connect(lambda: self.spb3.setValue((self.vs3.value()*3.6, 3.6*0.75*self.vs3.value(), 3.6*0.5*self.vs3.value())))

        self.vs4.valueChanged.connect(lambda: self.spb6.setValue((self.vs4.value(), self.vs4.value()*0.9, self.vs4.value()*0.7, self.vs4.value()*0.6, self.vs4.value()*0.5)))
        self.vs4.valueChanged.connect(lambda: self.spb7.setValue((self.vs4.value(), self.vs4.value(), self.vs4.value())))


def main():
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

