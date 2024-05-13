from PyQt6.QtCore import QObject, pyqtSignal

class NumbersModel(QObject):
    changed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._a = 0
        self._b = 50
        self._c = 100
        self.openData()

    def _update(self):
        self.changed.emit()

    def openData(self):
        try:
            with open("saved_data.txt") as f:
                s = f.read()
                if len(s) > 0:
                    a, b, c = map(int, s.split(" "))
                    self._a = max(0, min(a, 100))  # Ограничение от 0 до 100
                    self._b = max(self._a, min(b, 100))  # B не меньше A и не больше C
                    self._c = max(self._b, min(c, 100))  # Ограничение от B до 100
        except FileNotFoundError:
            pass

    def saveData(self):
        with open("saved_data.txt", "w") as f:
            s = " ".join(str(item) for item in self.getValues())
            f.write(s)

    def setA(self, value):
        try:
            value = int(value)
        except ValueError:
            return
        if value >= 0 and value <= 100:
            self._a = value
            if self._a > self._b:
                self._b = self._a
            if self._b > self._c:
                self._c = self._b
            self._update()

    def setB(self, value):
        try:
            value = int(value)
        except ValueError:
            return
        if value >= 0 and value <= 100:
            if value < self._a:
                self._b = self._a
            elif value > self._c:
                self._b = self._c
            else:
                self._b = value
            self._update()

    def setC(self, value):
        try:
            value = int(value)
        except ValueError:
            return
        if value >= 0 and value <= 100:
            self._c = value
            if self._c < self._b:
                self._b = self._c
            if self._b < self._a:
                self._a = self._b
            self._update()

    def getValues(self):
        return [self._a, self._b, self._c]

    def getA(self):
        return self._a

    def getB(self):
        return self._b

    def getC(self):
        return self._c
