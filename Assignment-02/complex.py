class Complex:
    def __init__(self, real, imaginary):
        self._real = real
        self._imaginary = imaginary

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        self._real = value

    @property
    def imaginary(self):
        return self._imaginary

    @imaginary.setter
    def imaginary(self, value):
        self._imaginary = value

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        """Override the default Unequal behavior"""
        return self.real != other.real or self.imaginary != other.imaginary
