class Contestant:
    def __init__(self, p1: int, p2: int, p3: int):
        if p1 > 10 or p1 < 0 or p2 > 10 or p2 < 0 or p3 > 10 or p3 < 0:
            raise ValueError('Value either greater than 10 or smaller than 0')
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

    @property
    def p1(self):
        return self._p1

    @p1.setter
    def p1(self, value: int):
        if value > 10 or value < 0:
            raise ValueError('Value either greater than 10 or smaller than 0')
        self._p1 = value

    @property
    def p2(self):
        return self._p2

    @p2.setter
    def p2(self, value: int):
        if value > 10 or value < 0:
            raise ValueError('Value either greater than 10 or smaller than 0')
        self._p2 = value

    @property
    def p3(self):
        return self._p3

    @p3.setter
    def p3(self, value: int):
        if value > 10 or value < 0:
            raise ValueError('Value either greater than 10 or smaller than 0')
        self._p3 = value

    @property
    def average(self):
        return (self._p1+self._p2+self._p3)/3
