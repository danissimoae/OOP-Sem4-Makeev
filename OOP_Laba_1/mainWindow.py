# Form implementation generated from reading ui file 'Laba1DanilV3.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 731)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(812, 731))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(32, 9, 111, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelNums = QtWidgets.QLabel(parent=self.layoutWidget)
        self.labelNums.setObjectName("labelNums")
        self.verticalLayout.addWidget(self.labelNums)
        self.listWidgetNum = QtWidgets.QListWidget(parent=self.layoutWidget)
        self.listWidgetNum.setObjectName("listWidgetNum")
        self.verticalLayout.addWidget(self.listWidgetNum)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButtonAddNum = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButtonAddNum.setObjectName("pushButtonAddNum")
        self.verticalLayout.addWidget(self.pushButtonAddNum)
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.verticalLayout.addWidget(self.pushButtonClear)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.groupBoxTimer = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxTimer.setGeometry(QtCore.QRect(150, 4, 293, 491))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBoxTimer.setFont(font)
        self.groupBoxTimer.setObjectName("groupBoxTimer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxTimer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout2 = QtWidgets.QVBoxLayout()
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.pushButtonSetT = QtWidgets.QPushButton(parent=self.groupBoxTimer)
        self.pushButtonSetT.setObjectName("pushButtonSetT")
        self.verticalLayout2.addWidget(self.pushButtonSetT)
        self.labelTimer = QtWidgets.QLabel(parent=self.groupBoxTimer)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.labelTimer.setFont(font)
        self.labelTimer.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.labelTimer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTimer.setObjectName("labelTimer")
        self.verticalLayout2.addWidget(self.labelTimer)
        self.pushButtonStart = QtWidgets.QPushButton(parent=self.groupBoxTimer)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.verticalLayout2.addWidget(self.pushButtonStart)
        self.pushButtonPause = QtWidgets.QPushButton(parent=self.groupBoxTimer)
        self.pushButtonPause.setObjectName("pushButtonPause")
        self.verticalLayout2.addWidget(self.pushButtonPause)
        self.pushButtonReset = QtWidgets.QPushButton(parent=self.groupBoxTimer)
        self.pushButtonReset.setObjectName("pushButtonReset")
        self.verticalLayout2.addWidget(self.pushButtonReset)
        self.verticalLayout_2.addLayout(self.verticalLayout2)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(440, 10, 328, 679))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widgetDial = QtWidgets.QWidget(parent=self.gridLayoutWidget)
        self.widgetDial.setMinimumSize(QtCore.QSize(150, 200))
        self.widgetDial.setMaximumSize(QtCore.QSize(150, 200))
        self.widgetDial.setObjectName("widgetDial")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widgetDial)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.widgetDial)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_5.addWidget(self.lcdNumber)
        self.dial = QtWidgets.QDial(parent=self.widgetDial)
        self.dial.setMaximum(220)
        self.dial.setPageStep(1)
        self.dial.setObjectName("dial")
        self.verticalLayout_5.addWidget(self.dial)
        self.gridLayout.addWidget(self.widgetDial, 4, 0, 1, 1)
        self.frame_color = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.frame_color.setMinimumSize(QtCore.QSize(170, 440))
        self.frame_color.setMaximumSize(QtCore.QSize(170, 16777215))
        self.frame_color.setStyleSheet("")
        self.frame_color.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_color.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_color.setObjectName("frame_color")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_color)
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_color_5 = QtWidgets.QLabel(parent=self.frame_color)
        self.label_color_5.setMinimumSize(QtCore.QSize(150, 150))
        self.label_color_5.setMaximumSize(QtCore.QSize(150, 150))
        self.label_color_5.setStyleSheet("background-color: rgb(0, 200, 0);\n"
"border-radius: 75px;")
        self.label_color_5.setText("")
        self.label_color_5.setObjectName("label_color_5")
        self.verticalLayout_7.addWidget(self.label_color_5)
        self.widget_color_sliders_5 = QtWidgets.QWidget(parent=self.frame_color)
        self.widget_color_sliders_5.setMinimumSize(QtCore.QSize(80, 220))
        self.widget_color_sliders_5.setMaximumSize(QtCore.QSize(16777215, 210))
        self.widget_color_sliders_5.setObjectName("widget_color_sliders_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_color_sliders_5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.vertical_slider_r_5 = QtWidgets.QSlider(parent=self.widget_color_sliders_5)
        self.vertical_slider_r_5.setMinimumSize(QtCore.QSize(20, 200))
        self.vertical_slider_r_5.setMaximumSize(QtCore.QSize(16777215, 200))
        self.vertical_slider_r_5.setMaximum(255)
        self.vertical_slider_r_5.setSingleStep(1)
        self.vertical_slider_r_5.setPageStep(1)
        self.vertical_slider_r_5.setProperty("value", 0)
        self.vertical_slider_r_5.setSliderPosition(0)
        self.vertical_slider_r_5.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.vertical_slider_r_5.setObjectName("vertical_slider_r_5")
        self.horizontalLayout_10.addWidget(self.vertical_slider_r_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.vertical_slider_g_5 = QtWidgets.QSlider(parent=self.widget_color_sliders_5)
        self.vertical_slider_g_5.setMinimumSize(QtCore.QSize(20, 200))
        self.vertical_slider_g_5.setMaximumSize(QtCore.QSize(16777215, 200))
        self.vertical_slider_g_5.setMaximum(255)
        self.vertical_slider_g_5.setPageStep(1)
        self.vertical_slider_g_5.setProperty("value", 200)
        self.vertical_slider_g_5.setSliderPosition(200)
        self.vertical_slider_g_5.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.vertical_slider_g_5.setObjectName("vertical_slider_g_5")
        self.horizontalLayout_10.addWidget(self.vertical_slider_g_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.vertical_slider_b_5 = QtWidgets.QSlider(parent=self.widget_color_sliders_5)
        self.vertical_slider_b_5.setMinimumSize(QtCore.QSize(20, 200))
        self.vertical_slider_b_5.setMaximumSize(QtCore.QSize(16777215, 200))
        self.vertical_slider_b_5.setMaximum(255)
        self.vertical_slider_b_5.setPageStep(1)
        self.vertical_slider_b_5.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.vertical_slider_b_5.setObjectName("vertical_slider_b_5")
        self.horizontalLayout_10.addWidget(self.vertical_slider_b_5)
        self.verticalLayout_7.addWidget(self.widget_color_sliders_5)
        self.widget_line_edit_5 = QtWidgets.QWidget(parent=self.frame_color)
        self.widget_line_edit_5.setMinimumSize(QtCore.QSize(150, 20))
        self.widget_line_edit_5.setObjectName("widget_line_edit_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_line_edit_5)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.line_edit_r_5 = QtWidgets.QLineEdit(parent=self.widget_line_edit_5)
        self.line_edit_r_5.setMinimumSize(QtCore.QSize(50, 20))
        self.line_edit_r_5.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.line_edit_r_5.setMaxLength(3)
        self.line_edit_r_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_edit_r_5.setObjectName("line_edit_r_5")
        self.horizontalLayout_11.addWidget(self.line_edit_r_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.line_edit_g_5 = QtWidgets.QLineEdit(parent=self.widget_line_edit_5)
        self.line_edit_g_5.setMinimumSize(QtCore.QSize(50, 20))
        self.line_edit_g_5.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.line_edit_g_5.setMaxLength(3)
        self.line_edit_g_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_edit_g_5.setObjectName("line_edit_g_5")
        self.horizontalLayout_11.addWidget(self.line_edit_g_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.line_edit_b_5 = QtWidgets.QLineEdit(parent=self.widget_line_edit_5)
        self.line_edit_b_5.setMinimumSize(QtCore.QSize(50, 20))
        self.line_edit_b_5.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.line_edit_b_5.setMaxLength(3)
        self.line_edit_b_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_edit_b_5.setObjectName("line_edit_b_5")
        self.horizontalLayout_11.addWidget(self.line_edit_b_5)
        self.verticalLayout_7.addWidget(self.widget_line_edit_5)
        self.gridLayout.addWidget(self.frame_color, 2, 1, 1, 1)
        self.labelCoord = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelCoord.setFont(font)
        self.labelCoord.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.labelCoord.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelCoord.setObjectName("labelCoord")
        self.gridLayout.addWidget(self.labelCoord, 3, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.gridLayoutWidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(100, 100))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.labelVkladka1 = QtWidgets.QLabel(parent=self.tab)
        self.labelVkladka1.setGeometry(QtCore.QRect(0, 10, 141, 241))
        self.labelVkladka1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelVkladka1.setObjectName("labelVkladka1")
        self.checkBoxPic1 = QtWidgets.QCheckBox(parent=self.tab)
        self.checkBoxPic1.setGeometry(QtCore.QRect(0, 310, 151, 20))
        self.checkBoxPic1.setObjectName("checkBoxPic1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.labelVkladka2 = QtWidgets.QLabel(parent=self.tab_2)
        self.labelVkladka2.setGeometry(QtCore.QRect(0, 10, 141, 241))
        self.labelVkladka2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelVkladka2.setObjectName("labelVkladka2")
        self.checkBoxPic2 = QtWidgets.QCheckBox(parent=self.tab_2)
        self.checkBoxPic2.setGeometry(QtCore.QRect(0, 310, 151, 20))
        self.checkBoxPic2.setObjectName("checkBoxPic2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.widgetClicker = QtWidgets.QWidget(parent=self.gridLayoutWidget)
        self.widgetClicker.setObjectName("widgetClicker")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widgetClicker)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButtonClicker = QtWidgets.QPushButton(parent=self.widgetClicker)
        self.pushButtonClicker.setMinimumSize(QtCore.QSize(100, 150))
        self.pushButtonClicker.setStyleSheet("background-color: rgb(255, 204, 255);")
        self.pushButtonClicker.setObjectName("pushButtonClicker")
        self.verticalLayout_8.addWidget(self.pushButtonClicker)
        self.gridLayout.addWidget(self.widgetClicker, 4, 1, 1, 1)
        self.widgetComboBox = QtWidgets.QWidget(parent=self.centralwidget)
        self.widgetComboBox.setGeometry(QtCore.QRect(20, 500, 161, 161))
        self.widgetComboBox.setObjectName("widgetComboBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widgetComboBox)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelComboBox = QtWidgets.QLabel(parent=self.widgetComboBox)
        self.labelComboBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelComboBox.setObjectName("labelComboBox")
        self.verticalLayout_3.addWidget(self.labelComboBox)
        self.comboBox = QtWidgets.QComboBox(parent=self.widgetComboBox)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.groupBoxPassword = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxPassword.setGeometry(QtCore.QRect(190, 500, 231, 171))
        self.groupBoxPassword.setObjectName("groupBoxPassword")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBoxPassword)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButtonWeak = QtWidgets.QRadioButton(parent=self.groupBoxPassword)
        self.radioButtonWeak.setObjectName("radioButtonWeak")
        self.verticalLayout_4.addWidget(self.radioButtonWeak)
        self.radioButtonGood = QtWidgets.QRadioButton(parent=self.groupBoxPassword)
        self.radioButtonGood.setObjectName("radioButtonGood")
        self.verticalLayout_4.addWidget(self.radioButtonGood)
        self.radioButtonStrong = QtWidgets.QRadioButton(parent=self.groupBoxPassword)
        self.radioButtonStrong.setObjectName("radioButtonStrong")
        self.verticalLayout_4.addWidget(self.radioButtonStrong)
        self.textEditPassword = QtWidgets.QTextEdit(parent=self.groupBoxPassword)
        self.textEditPassword.setObjectName("textEditPassword")
        self.verticalLayout_4.addWidget(self.textEditPassword)
        self.groupBoxSpin = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxSpin.setGeometry(QtCore.QRect(30, 330, 111, 161))
        self.groupBoxSpin.setObjectName("groupBoxSpin")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBoxSpin)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(parent=self.groupBoxSpin)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_6.addWidget(self.lcdNumber_2)
        self.spinBox = QtWidgets.QSpinBox(parent=self.groupBoxSpin)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_6.addWidget(self.spinBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 21))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(parent=self.menubar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабараторная 1"))
        self.labelNums.setText(_translate("MainWindow", "Список значений"))
        self.pushButtonAddNum.setText(_translate("MainWindow", "Добавить"))
        self.pushButtonClear.setText(_translate("MainWindow", "Очистить"))
        self.groupBoxTimer.setTitle(_translate("MainWindow", "Таймер"))
        self.pushButtonSetT.setText(_translate("MainWindow", "Установить таймер"))
        self.labelTimer.setText(_translate("MainWindow", "00:00:00"))
        self.pushButtonStart.setText(_translate("MainWindow", "Старт"))
        self.pushButtonPause.setText(_translate("MainWindow", "Пауза"))
        self.pushButtonReset.setText(_translate("MainWindow", "Сброс"))
        self.line_edit_r_5.setText(_translate("MainWindow", "0"))
        self.line_edit_g_5.setText(_translate("MainWindow", "200"))
        self.line_edit_b_5.setText(_translate("MainWindow", "0"))
        self.labelCoord.setText(_translate("MainWindow", "(0 ; 0)"))
        self.labelVkladka1.setText(_translate("MainWindow", "Вкладка 1"))
        self.checkBoxPic1.setText(_translate("MainWindow", "Показать картинку"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.labelVkladka2.setText(_translate("MainWindow", "Вкладка 2"))
        self.checkBoxPic2.setText(_translate("MainWindow", "Показать картинку"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.pushButtonClicker.setText(_translate("MainWindow", "0"))
        self.labelComboBox.setText(_translate("MainWindow", "Выберите версию Python"))
        self.groupBoxPassword.setTitle(_translate("MainWindow", "Генератор паролей"))
        self.radioButtonWeak.setText(_translate("MainWindow", "Создать слабый пароль"))
        self.radioButtonGood.setText(_translate("MainWindow", "Создать хороший пароль"))
        self.radioButtonStrong.setText(_translate("MainWindow", "Создать надежный пароль"))
        self.groupBoxSpin.setTitle(_translate("MainWindow", "Введите значение"))
        self.menuMain.setTitle(_translate("MainWindow", "Главная"))