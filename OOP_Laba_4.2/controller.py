from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QMainWindow

from ui import Ui_MainWindow
from model import NumbersModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = NumbersModel()
        self.model.changed.connect(self.updateData)

        intValidator = QIntValidator(0, 100)
        self.ui.lineEditA.setValidator(intValidator)
        self.ui.lineEditB.setValidator(intValidator)
        self.ui.lineEditC.setValidator(intValidator)

        self.ui.lineEditA.editingFinished.connect(
            lambda: self.model.setA(self.ui.lineEditA.text())
        )
        self.ui.lineEditB.editingFinished.connect(
            lambda: self.model.setB(self.ui.lineEditB.text())
        )
        self.ui.lineEditC.editingFinished.connect(
            lambda: self.model.setC(self.ui.lineEditC.text())
        )

        self.ui.spinBoxA.valueChanged.connect(
            lambda: self.model.setA(self.ui.spinBoxA.value())
        )
        self.ui.spinBoxB.valueChanged.connect(
            lambda: self.model.setB(self.ui.spinBoxB.value())
        )
        self.ui.spinBoxC.valueChanged.connect(
            lambda: self.model.setC(self.ui.spinBoxC.value())
        )

        self.ui.horizontalSliderA.valueChanged.connect(
            lambda: self.model.setA(self.ui.horizontalSliderA.value())
        )
        self.ui.horizontalSliderB.valueChanged.connect(
            lambda: self.model.setB(self.ui.horizontalSliderB.value())
        )
        self.ui.horizontalSliderC.valueChanged.connect(
            lambda: self.model.setC(self.ui.horizontalSliderC.value())
        )


        self.updateData()

    def updateData(self):
        self.ui.lineEditA.setText(str(self.model.getA()))
        self.ui.spinBoxA.setValue(self.model.getA())
        self.ui.horizontalSliderA.setValue(self.model.getA())
        self.ui.labelA.setText(str(self.model.getA()))

        self.ui.lineEditB.setText(str(self.model.getB()))
        self.ui.spinBoxB.setValue(self.model.getB())
        self.ui.horizontalSliderB.setValue(self.model.getB())
        self.ui.labelB.setText(str(self.model.getB()))

        self.ui.lineEditC.setText(str(self.model.getC()))
        self.ui.spinBoxC.setValue(self.model.getC())
        self.ui.horizontalSliderC.setValue(self.model.getC())
        self.ui.labelC.setText(str(self.model.getC()))

        self.model.saveData()

