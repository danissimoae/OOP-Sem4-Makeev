import Laba1DanilV4
import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QInputDialog, QPushButton
from PyQt6.QtGui import QPixmap, QIntValidator, QPainter, QColor


class labaApp(QtWidgets.QMainWindow, Laba1DanilV4.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле
        # Вызываем метод из родительского класса
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        
        # Объект - Событие - Метод - Функция
        # pushButtonAddNum - имя оьъекта, определенного в файле дизайна
        # clicked - событие, которые относится к виджету
        # connect() - метод, который привязывает событие
        # к вызову переданной функции

        # Виджет pushButtonAddNum
        self.pushButtonAddNum.clicked.connect(self.addToListWidgetNums)
        self.pushButtonClear.clicked.connect(self.clearListWidgetNums)


        # Отрисовка pixMap
        self.checkBoxPic1.stateChanged.connect(self.checkBoxPixMap)
        self.checkBoxPic2.stateChanged.connect(self.checkBoxPixMap)


        # Изменение цветов
        self.vertical_slider_r_5.valueChanged.connect(self.setColorSliders)
        self.vertical_slider_g_5.valueChanged.connect(self.setColorSliders)
        self.vertical_slider_b_5.valueChanged.connect(self.setColorSliders)
        self.validator = QIntValidator(0, 999)
        self.line_edit_r_5.setValidator(self.validator)
        self.line_edit_g_5.setValidator(self.validator)
        self.line_edit_b_5.setValidator(self.validator)
        self.line_edit_r_5.editingFinished.connect(self.setColorLineEdit)
        self.line_edit_g_5.editingFinished.connect(self.setColorLineEdit)
        self.line_edit_b_5.editingFinished.connect(self.setColorLineEdit)


        # Dial + Lcd
        self.dial.setMaximum(100)
        self.dial.valueChanged.connect(self.dialLcd)


        # widgetClicker
        self.clickerCount = 0
        self.pushButtonClicker.clicked.connect(self.clicker)


        # spinLcd
        self.spinBox.valueChanged.connect(self.spinLcd)

        
        # comboBoxPython
        self.comboBox.addItems(['Python 1.0', 'Python 3.0', 'Python 3.7'])
        self.comboBox.activated.connect(self.comboBoxPython)

        # groupBoxPassword
        self.textEditPassword.setReadOnly(True)
        self.radioButtonWeak.toggled.connect(self.passwordGenerator)
        self.radioButtonGood.toggled.connect(self.passwordGenerator)
        self.radioButtonStrong.toggled.connect(self.passwordGenerator)


        # Виджет таймер
        self.timerCount = 0
        self.startFlag = False
        self.pushButtonSetT.clicked.connect(self.setTime)
        self.pushButtonStart.clicked.connect(self.startTimer)
        self.pushButtonPause.clicked.connect(self.pauseTimer)
        self.pushButtonReset.clicked.connect(self.resetTimer)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.time)
        self.timer.start(100)


        # Обновление лейбла координат
        #self.timer.timeout.connect(self.updateCursor)

        # Динамическое создание и удаление объектов
        self.objectCount = 0
        self.pushButtonCreate.clicked.connect(self.createObject)

        # Paint
        self.mouseDoubleClickEvent = self.createObject
        self.resizeEvent = self.getNewSize
        

#################### Функции обработчики ######################################
###############################################################################

    def addToListWidgetNums(self):
        '''
        Обработчик для lineEditNum
        '''
        text = self.lineEdit.text()
        if (not text.isspace()) and text not in [self.listWidgetNum.item(i).text() for i in range(self.listWidgetNum.count())]:
            self.listWidgetNum.addItem(text)
            self.lineEdit.clear()

    def clearListWidgetNums(self):
        self.listWidgetNum.clear()

###############################################################################
###############################################################################

    def time(self):
        '''
        Алгоритм отсчета времени и обновления лейбла
        '''
        if self.startFlag:
            self.timerCount -= 1
            if self.timerCount == 0:
                self.startFlag = False
                self.labelTimer.setText("Завершено")
        
        if self.startFlag:
            timerText = str(self.timerCount / 10) + " с"
            self.labelTimer.setText(timerText)

    
    def setTime(self):
        '''
        Установка времени
        '''
        self.startFlag = False
        second, done = QInputDialog.getInt(self, 'Секунды', 'Введите секунды:')

        if done and second >= 0:
            self.timerCount = second * 10
            self.labelTimer.setText(str(second))


    def startTimer(self):
        '''
        Обработчик для виджета pushButtonStart
        '''
        self.startFlag = True
        if self.timerCount == 0:
            self.startFlag = False


    def pauseTimer(self):
        '''
        Обработчик для виджета pushButtonPause
        '''
        self.startFlag = False


    def resetTimer(self):
        '''
        Обработчик для виджета pushbuttonReset
        '''
        self.startFlag = False
        self.timerCount = 0
        self.labelTimer.setText('0')

###############################################################################
###############################################################################

    def checkBoxPixMap(self):
        if self.checkBoxPic1.isChecked():
            self.labelVkladka1.show()
            self.labelVkladka1.setPixmap(QPixmap('tab1').scaled(200, 200))
        else:
            self.labelVkladka1.hide()

        if self.checkBoxPic2.isChecked():
            self.labelVkladka2.show()
            self.labelVkladka2.setPixmap(QPixmap('tab2').scaled(200, 200))
        else:
            self.labelVkladka2.hide()

###############################################################################
###############################################################################

    def mouseMoveEvent(self, event):
        '''
        Обновление лейбла координат курсора
        '''
        self.labelCoord.setText(f"{event.pos().x()}, {event.pos().y()}")

###############################################################################
###############################################################################

    def setColorSliders(self):
        '''
        Обработчик для слайдеров
        '''
        r = self.vertical_slider_r_5.value()
        g = self.vertical_slider_g_5.value()
        b = self.vertical_slider_b_5.value()
        self.label_color_5.setStyleSheet(
        f"\
            border-radius: 75px;\
            background-color: rgb({r}, {g}, {b});\
        "
        )
        self.line_edit_r_5.setText(f"{r}")
        self.line_edit_g_5.setText(f"{g}")
        self.line_edit_b_5.setText(f"{b}")
    
    def setColorLineEdit(self):
        '''
        Обработчик для лайнэдитов цветного шара
        '''
        if int(self.sender().text()) > 255:
            self.sender().setText("255")
        r = int(self.line_edit_r_5.text())
        g = int(self.line_edit_g_5.text())
        b = int(self.line_edit_b_5.text())
        self.label_color_5.setStyleSheet(
            f"\
            border-radius: 75px;\
            background-color: rgb({r}, {g}, {b});\
            "
        )
        self.vertical_slider_r_5.setValue(r)
        self.vertical_slider_g_5.setValue(g)
        self.vertical_slider_b_5.setValue(b)

###############################################################################
###############################################################################

    def dialLcd(self):
        value = self.dial.value()
        self.lcdNumber.display(value)

###############################################################################
###############################################################################

    def clicker(self):
        self.clickerCount += 1
        self.pushButtonClicker.setText(str(self.clickerCount))

###############################################################################
###############################################################################

    def spinLcd(self):
        self.lcdNumber_2.display(self.spinBox.value())

###############################################################################
###############################################################################

    def comboBoxPython(self):
        info = ['январь 1994 года',
                '16 октября 2000 года',
                '3 декабря 2008 года']
        self.labelComboBox.setText(info[self.comboBox.currentIndex()])

###############################################################################
###############################################################################

    def passwordGenerator(self):
        if self.radioButtonWeak.isChecked():
            self.textEditPassword.setText("qwerty1234")
        if self.radioButtonGood.isChecked():
            self.textEditPassword.setText("RybaMech1337")
        if self.radioButtonStrong.isChecked():
            self.textEditPassword.setText("qCtZ3XCoOsP0%357_3lOp")

###############################################################################
###############################################################################

    def createObject(self, event):
        self.objectCount += 1
        newButton = QPushButton('Кнопка')
        newButton.clicked.connect(lambda: self.removeObject(newButton))
        if self.objectCount <= 8:
            self.layoutCreatingZone.addWidget(newButton)

    def removeObject(self, button):
        self.objectCount -= 1
        self.layoutCreatingZone.removeWidget(button)
        button.deleteLater()


###############################################################################
###############################################################################

    def getNewSize(self, event):
        self.labelComboBox.setText(f"{self.size().width()}x{self.size().height()}")
    
###############################################################################
###############################################################################

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = labaApp()
    window.show()
    app.exec()



if __name__ == '__main__':
    main()
    