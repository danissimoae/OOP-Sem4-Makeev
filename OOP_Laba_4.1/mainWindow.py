from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QCheckBox
from canvas import Canvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._canvas = Canvas(self, 20, 20, 500, 500)

        self._checkBoxCtrl = QCheckBox(self)
        self._checkBoxCtrl.stateChanged.connect(
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
        self.setFixedSize(720, 560)

        self._checkBoxSelectAll.setGeometry(540, 40, 200, 50)
        self._checkBoxSelectAll.setText("All selected")

        self._checkBoxCtrl.setGeometry(540, 90, 200, 50)
        self._checkBoxCtrl.setText("Ctrl enabled")


    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Delete:
            self._canvas.deleteSelected()

        if event.key() == Qt.Key.Key_Control and self._checkBoxCtrl.isChecked():
            self._canvas.setSelectFew(True)


    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key.Key_Control and self._checkBoxCtrl.isChecked():
            self._canvas.setSelectFew(False)

