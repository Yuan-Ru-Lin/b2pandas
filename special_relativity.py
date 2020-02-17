import pandas as pd
import numpy as np


class Vector3D:

    def __init__(self, c1, c2, c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    def Magnitude(self):
        return np.sqrt(self.c1 ** 2 + self.c2 ** 2 + self.c3 ** 2)

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.c1 * other.c1 + self.c2 * other.c2 + self.c3 * other.c3
        else:
            return Vector3D(self.c1 * other, self.c2 * other, self.c3 * other)

    def __add__(self, other):
        assert isinstance(other, Vector3D), "You must add another Vector3D!"
        return Vector3D(self.c1 + other.c1, self.c2 + other.c2, self.c3 + other.c3)

    def __sub__(self, other):
        assert isinstance(other, Vector3D), "You must subtract another Vector3D!"
        return Vector3D(self.c1 - other.c1, self.c2 - other.c2, self.c3 - other.c3)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, divisor: float):
        return Vector3D(self.c1 / divisor, self.c2 / divisor, self.c3 / divisor)

    def __str__(self):
        return "x:\n{0},\ny:\n{1},\nz:\n{2}".format(self.c1, self.c2, self.c3)


class FourMomentum:

    def __init__(self, c0, c1, c2, c3):
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

    @classmethod
    def from3Momentum(cls, energy, threeMomentum: Vector3D):
        return cls(c0=energy, c1=threeMomentum.c1, c2=threeMomentum.c2, c3=threeMomentum.c3)

    def __add__(self, other):
        return FourMomentum(self.c0 + other.c0, self.c1 + other.c1, self.c2 + other.c2, self.c3 + other.c3)

    def __sub__(self, other):
        return FourMomentum(self.c0 - other.c0, self.c1 - other.c1, self.c2 - other.c2, self.c3 - other.c3)

    def __mul__(self, other):
        return self.c0 * other.c0 - self.c1 * other.c1 - self.c2 * other.c2 - self.c3 * other.c3

    def __truediv__(self, divisor: float):
        return FourMomentum(self.c0 / divisor, self.c1 / divisor, self.c2 / divisor, self.c3 / divisor)

    def temporalPart(self):
        return self.c0

    def spatialPart(self):
        return Vector3D(self.c1, self.c2, self.c3)

    def invariantMass(self):
        return np.sqrt(self * self)

    def _LorentzFactor(self):
        return self.c0 / self.invariantMass()

    def _beta3D(self):
        return Vector3D(self.c1, self.c2, self.c3) / (self.invariantMass() * self._LorentzFactor())

    def boostedTo(self, targetedVelocity: Vector3D):
        b = targetedVelocity
        r = 1 / np.sqrt(1 - b.Magnitude()**2)
        c0 = r * (self.c0 - b.c1 * self.c1 - b.c2 * self.c2 - b.c3 * self.c3)
        c1 = (- r * b.c1 * self.c0
              + (1 + (r-1) * b.c1 * b.c1 / b.Magnitude()**2) * self.c1
              + (r-1) * b.c2 * b.c1 / b.Magnitude()**2 * self.c2
              + (r-1) * b.c3 * b.c1 / b.Magnitude()**2 * self.c3)
        c2 = (- r * b.c2 * self.c0
              + (r-1) * b.c1 * b.c2 / b.Magnitude()**2 * self.c1
              + (1 + (r-1) * b.c2 * b.c2 / b.Magnitude()**2) * self.c2
              + (r-1) * b.c3 * b.c2 / b.Magnitude()**2 * self.c3)
        c3 = (- r * b.c3 * self.c0
              + (r-1) * b.c1 * b.c3 / b.Magnitude()**2 * self.c1
              + (r-1) * b.c2 * b.c3 / b.Magnitude()**2 * self.c2
              + (1 + (r-1) * b.c3 * b.c3 / b.Magnitude()**2) * self.c3)
        return FourMomentum(c0, c1, c2, c3)
