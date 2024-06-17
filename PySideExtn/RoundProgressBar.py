#############################################################################################
# CREATOR:  ANJAL.P                                                                         #
# ON:       2020 SEP.                                                                       #
# AIM:      To Extend the capability of the PySide2 and PyQt5 Python library with easy to   #
#           use extension containing commonly used widgets which is not natively supported  #
#           by the Qt Frame work (or atleast for Python version of Qt).                     #
# VERSION:  v1.0.0                                                                          #
# NOTES:    CLASS : RoundProgressBar : Can be accessed by : importing                       #
#           from PySideExtn.RoundProgressBar import RoundProgressBar                       #
# REFER:    Github: https://github.com/anjalp/PySideExtn                                   #
#############################################################################################


from qtpy import QtWidgets, QtCore
from qtpy.QtCore import Qt, QSize, QEvent, QRectF
from qtpy.QtGui import QBrush, QColor, QPainter, QPen, QPaintEvent, QFont
from qtpy.QtWidgets import QStyleOption, QStyle


class RoundProgressBar(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(RoundProgressBar, self).__init__(parent)

        self.positionX = 0 
        self.positionY = 0
        self.posFactor = 0

        self.minimumSize = (0, 0)
        self.maximumSize = (0, 0)
        self.dynamicMin = True
        self.dynamicMax = True
        self.Size = 0
        self.sizeFactor = 0

        self.maximum = 100
        self.minimum = 0

        self.type = self.barStyleFlags.Donet
        self.startPosition = self.startPosFlags.North
        self.direction = self.rotationFlags.Clockwise

        self.textType = self.textFlags.Percentage
        self.textColor = (0, 159, 227)
        self.textWidth = self.Size/8
        self.textFont = 'Segoe UI'
        self.textValue = '12%'
        self.textRatio = 8
        self.textFactorX = 0
        self.textFactorY = 0
        self.dynamicText = True
        self.textActive = True

        self.lineWidth = 5
        self.pathWidth = 5
        self.lineStyle = self.lineStyleFlags.SolidLine
        self.lineCap = self.lineCapFlags.SquareCap
        self.lineColor = QColor(0, 159, 227)
        self.pathColor = (218, 218, 218)

        self.circleColor = (218, 218, 218)
        self.circleRatio = 0.8
        self.circlePosX = 0
        self.circlePosY = 0

        self.pieColor = (200, 200, 200)
        self.pieRatio = 1
        self.piePosX = 0
        self.piePosY = 0

        self._value = -45*16

        # if self.dynamicMin:
        self.setMinimumSize(QSize(self.lineWidth*6 + self.pathWidth*6, self.lineWidth*6 + self.pathWidth*6))

#------------------------------------------------------CLASS ENUMERATORS
    class lineStyleFlags:
        SolidLine = Qt.SolidLine
        DotLine = Qt.DotLine
        DashLine = Qt.DashLine

    class lineCapFlags:
        SquareCap = Qt.SquareCap
        RoundCap = Qt.RoundCap

    class barStyleFlags:
        Donet = 0
        Line = 1
        Pie = 2
        Pizza = 3
        Hybrid1 = 4
        Hybrid2 = 5

    class rotationFlags:
        Clockwise = -1
        AntiClockwise = 1

    class textFlags:
        Value = 0
        Percentage = 1

    class startPosFlags:
        North = 90*16
        South = -90*16
        East = 0*16
        West = 180*16

#------------------------------------------------------METHODS FOR CHANGING THE PROPERTY OF THE ROUNDPROGRESSBAR :SOLTS
    def eventFilter(self, obj, e: QEvent):
        if obj is self.window():
            if e.type() == QEvent.Resize:
                re = QResizeEvent(e)
                self.resize(re.size())

        return super().eventFilter(obj, e)
    
    def resizeEvent(self, e):
        self.adjustSize()
    
    def showEvent(self, e):
        self.adjustSize()
        super().showEvent(e)

    def value(self):
        return self._value

    def setMaximumValue(self, maximum):
        """
        Maximum Value of the Progressbar
        ...

        Parameters
        --------------

        maximum : int
            Maximum value of the round progress bar

        Raises
        --------------
        Exception : Maximum and Minimum cannot be the Same
        """
        
        if self.minimum==maximum:               #FOR AVOIDING DIVISION BY ZERO ERROR IN FUTURE
            raise Exception("Maximum and Minimum cannot be the Same")
            return
        if self.maximum != maximum:
            self.maximum = maximum
            self.update()

    def setMinimumValue(self, minimum):
        """
        Minimum Value of the Progressbar
        ...

        Parameters
        --------------

        minimum : int
            Minimum value of the round progress bar

        Raises
        --------------
        Exception : Maximum and Minimum cannot be the Same
        """
        
        if self.minimum==maximum:               #FOR AVOIDING DIVISION BY ZERO ERROR IN FUTURE
            raise Exception("Maximum and Minimum cannot be the Same")
            return
        if self.minimum != minimum:
            self.minimum = minimum
            self.update()

    def setRange(self, maximum, minimum):
        """
        Range include the maximum and the minimum in one go.
        ...

        Parameters
        --------------

        maximum : int
            Maximum value of the round progress bar

        minimum : int
            Minimum value for the round progress bar

        Raises
        --------------
        none
        """
        
        if minimum > maximum:
            maximum, minimum = minimum, maximum
        if self.maximum != maximum:
            self.maximum = maximum
        if self.minimum != minimum:
            self.minimum = minimum
        self.update()

    def setInitialPos(self, pos):
        """
        Starting position of the round progress bar
        ...

        Parameters
        --------------

        pos : String
            Position string: 'North', 'South', 'East' and 'West'

        Raises
        --------------
        ValueError : Maximum and Minimum cannot be the Same
        """
        
        if pos=='North':
            self.startPosition = self.startPosFlags.North
        elif pos=='South':
            self.startPosition = self.startPosFlags.South
        elif pos=='East':
            self.startPosition = self.startPosFlags.East
        elif pos=='West':
            self.startPosition = self.startPosFlags.West
        else:
            raise Exception("Initial Position String can be: 'South', 'North'")
            return

    def setValue(self, value):
        """
        Set progress value
        ...

        Parameters
        --------------

        value : int
            The value of the progress bar in int. The value should be: min<=value<=max

        Raises
        --------------
        none
        """
        
        if value >= self.maximum:
            RoundProgressBar.convertInputValue(self, self.maximum)
        elif value < self.minimum:
            RoundProgressBar.convertInputValue(self, self.minimum)
        else:
            RoundProgressBar.convertInputValue(self, value)
        
        self._value =  value
        self.update()

    def reset(self):
        """
        Reset the progress bar to 0%
        ...

        Parameters
        --------------
        none

        Raises
        --------------
        none
        """
        
        RoundProgressBar.convertInputValue(self, self.minimum)
        self.update()

    def setGeometry(self, posX, posY):
        """
        Set the X and Y position of the round progress bar.
        ...

        Parameters
        --------------

        posX : int
            The position of the round progress bar in int for X axis.

        posY : int
            The position of the round progress bar in int for Y axis.

        Raises
        --------------
        none
        """
        
        if self.positionX != posX:
            self.positionX = posX
        if self.positionY != posY:
            self.positionY = posY
        self.update()

    def setLineWidth(self, width):
        """
        Line Width of the line in round progress bar.
        ...

        Parameters
        --------------

        width: int
            Line width corresponding to the width in px.

        Raises
        --------------
        Exception: Line Width should be in int
        """

        if type(width)!=type(5):
            raise Exception('Line Width should be in int')
            return
        if self.lineWidth != width:
            self.lineWidth = width
            self.update()

    def setLineColor(self, rgb):
        """
        Line Color of the progress bar.
        ...

        Parameters
        --------------

        rgb: tuple: (R, G, B)
            Color is passed as a tuple of values for red, blue and green in the order: (R, G, B)

        Raises
        --------------
        Exception: Line Color accepts a tuple: (R, G, B).
        """

        # if type(rgb)!=type(()):
        #     raise Exception("Line Color accepts a tuple: (R, G, B).")
        #     return
        # if self.lineColor != rgb:
        self.lineColor = QColor(rgb)
        self.update()

    def setPathColor(self, rgb):
        """
        Path Color settings.
        ...

        Parameters
        --------------

        rgb: tuple: (R, G, B)
            Color is passed as a tuple of values for red, blue and green in the order: (R, G, B)

        Raises
        --------------
        Exception: Path Color accepts a tuple: (R, G, B).
        """
        
        if type(rgb)!=type(()):
            raise Exception("Path Color accepts a tuple: (R, G, B).")
            return
        if self.pathColor != rgb:
            self.pathColor = rgb
            self.update()

    def setPathWidth(self, width):
        """
        Path width settings.
        ...

        Parameters
        --------------

        width: int
            Width of the path in px

        Raises
        --------------
        Exception: Line Width should be in int
        """

        if type(width)!=type(5):
            raise Exception('Path Width should be in int')
            return
        if self.pathWidth != width:
            self.pathWidth = width
            self.update()

    def setDirection(self, direction):
        """
        Direction of rotation of the progress bar.
        ...

        Parameters
        --------------

        direction: string
            string can be: 'AntiClockwise' or 'Clockwise'. Default: 'Clockwise'.

        Raises
        --------------
        Exception: Direction can only be: 'Clockwise' and 'AntiClockwise'
        """

        if direction == 'Clockwise' or direction == -1:
            self.direction = self.rotationFlags.Clockwise
        elif direction == 'AntiClockwise' or direction == 1:
            self.direction = self.rotationFlags.AntiClockwise
        else:
            raise Exception("Direction can only be: 'Clockwise' and 'AntiClockwise' and Not: " + str(direction))
            return
        self.update()

    def setBarStyle(self, style):
        """
        Bar Style of the progress bar.
        ...

        Parameters
        --------------

        style: String
            String of the styles of the progress bar: 'Donet', 'Pie', 'line', 'Hybrid1', 'Hybrid2', 'Pizza'

        Raises
        --------------
        Exception: Round Progress Bar has only the following styles: 'Line', 'Donet', 'Hybrid1', 'Pizza', 'Pie' and 'Hybrid2'
        """

        if style=='Donet':
            self.type = self.barStyleFlags.Donet
        elif style=='Line':
            self.type = self.barStyleFlags.Line
        elif style=='Pie':
            self.type = self.barStyleFlags.Pie
        elif style=='Pizza':
            self.type = self.barStyleFlags.Pizza
        elif style=='Hybrid1':
            self.type = self.barStyleFlags.Hybrid1
        elif style=='Hybrid2':
            self.type = self.barStyleFlags.Hybrid2
        else:
            raise Exception("Round Progress Bar has only the following styles: 'Line', 'Donet', 'Hybrid1', 'Pizza', 'Pie' and 'Hybrid2'")
            return
        self.update()

    def setLineStyle(self, style):
        """
        Line Style setting.
        ...

        Parameters
        --------------

        style: String
            Line style: 'DotLine', 'DashLine', 'SolidLine', passed as a string.

        Raises
        --------------
        none
        """

        if style == 'SolidLine':
            self.lineStyle = self.lineStyleFlags.SolidLine
        elif style == 'DotLine':
            self.lineStyle = self.lineStyleFlags.DotLine
        elif style == 'DashLine':
            self.lineStyle = self.lineStyleFlags.DashLine
        else:
            self.lineStyle = self.lineStyleFlags.SolidLine

    def setLineCap(self, cap):
        """
        Line Cap setting.
        ...

        Parameters
        --------------

        cap: String
            Cap is the end point of a stroke. It can be: 'RoundCap' or 'SquareCap'

        Raises
        --------------
        none
        """

        if cap=='SquareCap':
            self.lineCap = self.lineCapFlags.SquareCap
        elif cap == 'RoundCap':
            self.lineCap = self.lineCapFlags.RoundCap

    def setTextColor(self, rgb):
        """
        Text color of the text inside the progress bar
        ...

        Parameters
        --------------

        rgb: tuple
            Color of the text in the format: (R, G, B)

        Raises
        --------------
        none
        """

        # if self.textColor != rgb:
        self.textColor = rgb
        self.update()

    def setTextFont(self, font):
        """
        Font of the text inside the round progress bar
        ...

        Parameters
        --------------

        font: str
            Name of the font in string

        Raises
        --------------
        none
        """

        if self.textFont != font:
            self.textFont = font
            self.update()

    def setTextFormat(self, textTyp):
        """
        Text formatter i.e. the value or the percentage.
        ...

        Parameters
        --------------

        textTyp: str
            'value', 'percentage'

        Raises
        --------------
        none
        """

        if textTyp == 'Value':
            self.textType = self.textFlags.Value
        elif textTyp == 'Percentage':
            self.textType = self.textFlags.Percentage
        else:
            self.textType = self.textFlags.Percentage

    def setTextRatio(self, ratio):
        """
        Text ratio with respect to the size of the progress bar.
        ...

        Parameters
        --------------

        ratio: int
            In number from 3 to 50 corresponding to 1/3 or 1/50 the size of the roundprogressbar.

        Raises
        --------------
        none
        """

        if self.textRatio != ratio:
            if ratio < 3:
                ratio = 3
            elif ratio > 50:
                ratio = 50
            self.textRatio = ratio
            self.update()

    def setTextWidth(self, width):
        """
        Text Width.
        ...

        Parameters
        --------------

        font: int
            Text constant width. Will not change during the widget resize.

        Raises
        --------------
        none
        """

        self.dynamicText = False
        if width > 0:
            self.textWidth = width
            self.update()

    def setCircleColor(self, rgb):
        """
        Circle color fill inside the circle.
        ...

        Parameters
        --------------

        font: tuple
            The color of the circle in the tuple corresponding to the (R, G, B).

        Raises
        --------------
        none
        """

        if self.circleColor != rgb:
            self.circleColor = rgb
            self.update()

    def setCircleRatio(self, ratio):
        """
        Circle ration corresponding to the round progress bar.
        ...

        Parameters
        --------------

        font: int
            Integer corresponding to the size of the progress bar to that of the round progress bar.

        Raises
        --------------
        none
        """

        if self.circleRatio != ratio:
            self.circleRatio = ratio
            self.update()

    def setPieColor(self, rgb):
        """
        Pie color inside the fill.
        ...

        Parameters
        --------------

        font: tuple
            Tuple consist in format (R, G, B). Same as color setting to Line.

        Raises
        --------------
        none
        """

        if self.pieColor != rgb:
            self.pieColor = rgb
            self.update()

    def setPieRatio(self, ratio):
        """
        Pie Ratio
        ...

        Parameters
        --------------

        font: int
            Ratio corresponding to the size between the roundprogressbar and the pie size.

        Raises
        --------------
        none
        """

        if self.pieRatio != ratio:
            self.pieRatio = ratio
            self.update()

    def enableText(self, enable):
        """
        Makes the Text visible/Hidden
        ...

        Parameters
        --------------

        font: bool
            True: Text visible, False: Text invisible.

        Raises
        --------------
        none
        """

        if enable:
            self.textActive = enable
        else:
            self.textActive = enable
        self.update()


#------------------------------------------------------METHODS FOR GETTING THE PROPERTY OF ROUNDPROGRESSBAR SLOTS

    def getSize(self):
        """
        Get the present size of the progress bar.
        ...

        Returns
        --------------
        Return the size of the round progress bar in int.
        """

        return self.Size

    def getValue(self):
        """
        Present value of the progress bar.
        ...

        Returns
        --------------
        int corresponding to the present progress bar value.
        """

        return self._value/16

    def getRange(self):
        """
        Progress bar range.
        ...

        Returns
        --------------
        tuple consisting of minimu and maximum as elements.
        """

        return (self.minimum, self.maximum)

    def getTextWidth(self):
        """
        Text width of the present text in the central of the widget.
        ...

        Returns
        --------------
        int corresponding to the width of the text
        """

        return self.textWidth

#------------------------------------------------------ENGINE: WHERE ALL THE REAL STUFF TAKE PLACE: WORKING OF THE ROUNDPROGRESSBA

    def MinimumSize(self, dynamicMax, minimum, maximum):
        """
        Minimum size calculating code: Takes consideration of the width of the line/path/circle/pie and the user defined
        width and also the size of the frame/window of the application.

        """

        Height = self.height()
        Width = self.width()
        if dynamicMax:
            if Width >= Height and Height >= minimum[1]:
                self.Size = Height
            elif Width < Height and Width >= minimum[0]:
                self.Size = Width
        else:
            if Width >= Height and Height <= maximum[1]:
                self.Size = Height
            elif Width < Height and Width <= maximum[0]:
                self.Size = Width

    def convertInputValue(self, value):
        """
        CONVERTS ANY INPUT VALUE TO THE 0*16-360*16 DEGREE REFERENCE OF THE QPainter.drawArc NEEDED.

        """

        self._value = ((value - self.minimum)/(self.maximum - self.minimum))*360*16
        self._value = self.direction*self._value
        if self.textType==RoundProgressBar.textFlags.Percentage:
            self.textValue = str(round(((value - self.minimum)/(self.maximum - self.minimum))*100)) + "%"
        else:
            self.textValue = str(value)

    #SINCE THE THICKNESS OF THE LINE OR THE PATH CAUSES THE WIDGET TO WRONGLY FIT INSIDE THE SIZE OF THE WIDGET DESIGNED IN THE 
    #QTDESIGNER, THE CORRECTION FACTOR IS NECESSERY CALLED THE GEOMETRYFACTOR, WHICH CALCULATE THE TWO FACTORS CALLED THE
    #self.posFactor AND THE self.sizeFactor, CALCULATION THIS IS NECESSERY AS THE 
    def geometryFactor(self):
        if self.lineWidth > self.pathWidth:
            self.posFactor = self.lineWidth/2 + 1
            self.sizeFactor = self.lineWidth + 1
        else:
            self.posFactor = self.pathWidth/2 + 1
            self.sizeFactor = self.pathWidth + 1

    def textFactor(self):
        if self.dynamicText:
            self.textWidth = self.Size/self.textRatio
        self.textFactorX = self.posFactor + (self.Size - self.sizeFactor)/2 - self.textWidth*0.75*(len(self.textValue)/2)
        self.textFactorY = self.textWidth/2 + self.Size/2

    def circleFactor(self):
        self.circlePosX = self.positionX + self.posFactor +  ((self.Size)*(1 - self.circleRatio))/2
        self.circlePosY = self.positionY + self.posFactor + ((self.Size)*(1 - self.circleRatio))/2

    def pieFactor(self):
        self.piePosX = self.positionX + self.posFactor +  ((self.Size)*(1 - self.pieRatio))/2
        self.piePosY = self.positionY + self.posFactor + ((self.Size)*(1 - self.pieRatio))/2



    def paintEvent(self, event: QPaintEvent):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)
        
        #THIS BELOW CODE AMKE SURE THAT THE SIZE OF THE ROUNDPROGRESSBAR DOESNOT REDUCES TO ZERO WHEN THE USER RESIZES THE WINDOW
        if self.dynamicMin:
            self.setMinimumSize(QSize(self.lineWidth*6 + self.pathWidth*6, self.lineWidth*6 + self.pathWidth*6))

        self.setMinimumSize(self.size())

        RoundProgressBar.MinimumSize(self, self.dynamicMax, self.minimumSize, self.maximumSize)
        RoundProgressBar.geometryFactor(self)
        RoundProgressBar.textFactor(self)
        RoundProgressBar.circleFactor(self)
        RoundProgressBar.pieFactor(self)
        
        if self.type==0: #DONET TYPE
            RoundProgressBar.pathComponent(self)
            RoundProgressBar.lineComponent(self)
            RoundProgressBar.textComponent(self)
        elif self.type==1: #LINE TYPE
            RoundProgressBar.lineComponent(self)
            RoundProgressBar.textComponent(self)
        elif self.type==2: #Pie
            RoundProgressBar.pieComponent(self)
            RoundProgressBar.textComponent(self)
        elif self.type==3: #PIZZA
            RoundProgressBar.circleComponent(self)
            RoundProgressBar.lineComponent(self)
            RoundProgressBar.textComponent(self)
        elif self.type==4: #HYBRID1
            RoundProgressBar.circleComponent(self)
            RoundProgressBar.pathComponent(self)
            RoundProgressBar.lineComponent(self)
            RoundProgressBar.textComponent(self)
        elif self.type==5: #HYBRID2
            RoundProgressBar.pieComponent(self)
            RoundProgressBar.lineComponent(self)
            RoundProgressBar.textComponent(self)

        
    def lineComponent(self):
        linePainter = QPainter(self)
        linePainter.setRenderHint(QPainter.Antialiasing)
        
        penLine = QPen()
        penLine.setStyle(self.lineStyle)
        penLine.setWidth(self.lineWidth)
        penLine.setBrush(self.lineColor)
        penLine.setCapStyle(self.lineCap)
        penLine.setJoinStyle(Qt.RoundJoin)
        linePainter.setPen(penLine)
        
        # Calculate the start and end angles based on the value
        startAngle = 0  # Start angle for clockwise arc
        endAngle = startAngle - (self._value / self.maximum) * 360 * 16  # Convert value to angle (clockwise)

        # Define the rectangle where the arc will be drawn
        rect = QRectF(self.positionX + self.posFactor, self.positionY + self.posFactor,
                    self.size().width() - self.sizeFactor, self.size().height() - self.sizeFactor)

        # Draw the arc in clockwise direction
        linePainter.drawArc(rect, startAngle, endAngle)

        linePainter.end()

    def pathComponent(self):
        pathPainter = QPainter(self)
        pathPainter.setRenderHint(QPainter.Antialiasing)
        penPath = QPen()
        penPath.setStyle(Qt.SolidLine)
        penPath.setWidth(self.pathWidth)
        penPath.setBrush(QColor(self.pathColor[0], self.pathColor[1], self.pathColor[2]))
        penPath.setCapStyle(Qt.RoundCap)
        penPath.setJoinStyle(Qt.RoundJoin)
        pathPainter.setPen(penPath)
        pathPainter.drawArc(self.positionX + self.posFactor, self.positionY + self.posFactor, self.Size - self.sizeFactor, self.Size - self.sizeFactor, 0, 360*16)
        pathPainter.end()

    def textComponent(self):
        if self.textActive:
            textPainter = QPainter(self)
            penText = QPen()
            penText.setColor(QColor(self.textColor))
            textPainter.setPen(penText)
            fontText = QFont()
            fontText.setFamily(self.textFont)
            fontText.setPointSize(self.textWidth)
            textPainter.setFont(fontText)
            textPainter.drawText(self.positionX + self.textFactorX, self.positionY + self.textFactorY, self.textValue)
            textPainter.end()

    def circleComponent(self):
        circlePainter = QPainter(self)   
        penCircle = QPen()
        penCircle.setWidth(0)
        penCircle.setColor(QColor(self.circleColor[0], self.circleColor[1], self.circleColor[2]))
        circlePainter.setRenderHint(QPainter.Antialiasing)
        circlePainter.setPen(penCircle)
        circlePainter.setBrush(QColor(self.circleColor[0], self.circleColor[1], self.circleColor[2]))
        circlePainter.drawEllipse(self.circlePosX, self.circlePosY, (self.Size - self.sizeFactor)*self.circleRatio, (self.Size - self.sizeFactor)*self.circleRatio)

    def pieComponent(self):
        piePainter = QPainter(self)   
        penPie = QPen()
        penPie.setWidth(0)
        penPie.setColor(QColor(self.pieColor[0], self.pieColor[1], self.pieColor[2]))
        piePainter.setRenderHint(QPainter.Antialiasing)
        piePainter.setPen(penPie)
        piePainter.setBrush(QColor(self.pieColor[0], self.pieColor[1], self.pieColor[2]))
        piePainter.drawPie(self.piePosX, self.piePosY, (self.Size - self.sizeFactor)*self.pieRatio, (self.Size - self.sizeFactor)*self.pieRatio, self.startPosition, self._value)
