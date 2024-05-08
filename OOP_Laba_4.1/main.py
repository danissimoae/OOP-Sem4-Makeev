import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication
from mainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.setWindowTitle("Круги на форме")
    main_window.setWindowIcon(QIcon("windowIcon.png"))
    sys.exit(app.exec())
