from PyQt6.QtCore import QPoint, Qt
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen


class CCircle:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y
        self._R = 50
        self._isSelected = False


    def draw(self, canvas):
        painter = QPainter(canvas.getCanvasBase())
        center = QPoint(self._x, self._y)
        rx = self._R
        ry = rx

        if self._isSelected:
            painter.setBrush(QBrush(QColor(255,255,255,0)))
            painter.setPen(QPen(QColor(120,120,120),1))
            painter.drawRect(self._x - rx, self._y - ry, rx * 2, ry * 2)

        painter.setBrush(QBrush(QColor(79, 113, 190)))
        painter.setPen(QPen(QColor(0, 0, 0), 1))
        painter.drawEllipse(center, rx, ry)
        canvas.setPixmap(canvas.getCanvasBase())


    def isSelected(self):
        return self._isSelected

    def select(self):
        self._isSelected = True

    def unSelect(self):
        self._isSelected = False

    def isIncludeDot(self, pos: QPoint):
        x = pos.x()
        y = pos.y()
        return (x - self._x) ** 2 + (y - self._y) ** 2 <= self._R ** 2
