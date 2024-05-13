import sys
from PyQt6.QtWidgets import QApplication

from controller import MainWindow


def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    mainWindow.setWindowTitle('MVC')
    sys.exit(app.exec())


if __name__ == "__main__":
    main()