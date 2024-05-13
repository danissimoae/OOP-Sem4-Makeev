from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel
from ccircle import CCircle


class Canvas(QLabel):
    def __init__(self, parent, x, y, w, h):
        super().__init__(parent)
        self._container = []
        self._selectAll = False
        self._selectFew = False

        self._canvasBase = QPixmap(w, h)

        self._initUI(x, y, w, h)

    def _initUI(self, x: int, y: int, w: int, h: int):
        self.paint()

        self.setGeometry(x, y, w, h)
        self.setStyleSheet(
            """
                border: 3px solid rgb(0, 0, 0);
            """
        )

    def paint(self):
        self._canvasBase.fill(Qt.GlobalColor.white)
        for c in self._container:
            c.draw(self)
        self.setPixmap(self._canvasBase)

    def deleteSelected(self):
        newContainer = []
        for c in self._container:
            if c.isSelected():
                continue
            newContainer.append(c)
        self._container = newContainer
        if self._container:
            self._container[-1].select()
        self.paint()

    def setSelectAll(self, selectAll: bool):
        self._selectAll = selectAll

    def setSelectFew(self, selectFew: bool):
        self._selectFew = selectFew

    def getCanvasBase(self):
        return self._canvasBase

    def mousePressEvent(self, event):
        if not event.button() == Qt.MouseButton.LeftButton:
            return None

        position = event.pos()
        # Создавать ли объект
        flag = True


        if self._selectFew and event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            for i in range(len(self._container) - 1, -1, -1):
                circle = self._container[i]
                if circle.isIncludeDot(position):
                    circle.select()
                    break
            self.paint()
            return

        for c in self._container:
            c.unSelect()

        if self._selectAll:
            # Выделяем только те объекты, которые пересекаются с точкой клика
            for c in self._container:
                if c.isIncludeDot(position):
                    c.select()
            # Если есть пересекающиеся объекты, завершаем обработку
            if any(c.isSelected() for c in self._container):
                self.paint()
                return

        for i in range(len(self._container) - 1, -1, -1):
            circle = self._container[i]
            if circle.isIncludeDot(position):
                flag = False
                circle.select()
                # Если selectAll != True, останавливаемся после первого объекта
                if not self._selectAll:
                    break

        if flag:
            for c in self._container:
                c.unSelect()
            c = CCircle(position.x(), position.y())
            c.select()
            self._container.append(c)
        self.paint()
