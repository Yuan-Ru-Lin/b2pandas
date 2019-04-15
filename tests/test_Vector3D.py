import unittest
from ..special_relativity import Vector3D
import numpy as np
import pandas as pd


class TestVector3D(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame([[1, 2, 3, 4],
                                [2, 4, 5, 6],
                                [3, 3, 1, 7]])
        self.x = Vector3D(self.df[0], self.df[1], self.df[2])
        self.y = self.df[3]

    def tearDown(self):
        self.df = None
        self.x = None
        self.y = None

    def test__mul__(self):
        # Verify the multiplication in Vector3D * Vector3D (= Number)
        np.testing.assert_allclose(
            self.x * self.x, self.df[0]**2 + self.df[1]**2 + self.df[2]**2)

        # Verify the multiplication in Vector3D * Number (= Vector3D)
        self.assertTrue(self.x * self.y == Vector3D(
            self.df[0] * self.df[3], self.df[1] * self.df[3], self.df[2] * self.df[3]))
        self.assertTrue(self.x.__mul__(self.y) == Vector3D(
            self.df[0] * self.df[3], self.df[1] * self.df[3], self.df[2] * self.df[3]))

    def test__rmul__(self):
        pass
        # Verify the multiplication in Number * Vector3D (= Vector3D)
#         import pdb; pdb.set_trace()
#         self.assertTrue(self.y * self.x == Vector3D(self.df[0] * self.df[3], self.df[1] * self.df[3], self.df[2]* self.df[3]))


if __name__ == "__main__":
    unittest.main()
