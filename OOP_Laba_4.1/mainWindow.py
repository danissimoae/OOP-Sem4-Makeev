from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QCheckBox
from canvas import Canvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._canvas = Canvas(self, 20, 20, 500, 500)

        self._checkBoxCommand = QCheckBox(self)
        self._checkBoxCommand.stateChanged.connect(
            lambda: self._canvas.setSelectFew(False)
        )

        self._checkBoxSelectAll = QCheckBox(self)
        self._checkBoxSelectAll.stateChanged.connect(
            lambda: self._canvas.setSelectAll(self._checkBoxSelectAll.isChecked())
        )

        self._initUi()


    def _initUi(self):
        self.setStyleSheet(
            """
                background-color: rgb(255, 255, 255);
                color: rgb(0, 0, 0);
                font: 18pt;
            """
        )
        self.setFixedSize(770, 640)

        self._checkBoxSelectAll.setGeometry(640, 20, 110, 50)
        self._checkBoxSelectAll.setText("All")

        self._checkBoxCommand.setGeometry(640, 90, 110, 50)
        self._checkBoxCommand.setText("Command")


    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Delete:
            self._canvas.deleteSelected()

        if event.key() == Qt.Key.Key_Control and self._checkBoxCommand.isChecked():
            self._canvas.setSelectFew(True)


    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key.Key_Control and self._checkBoxCommand.isChecked():
            self._canvas.setSelectFew(False)

