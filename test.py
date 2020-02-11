from tests.test_Particle import TestParticle
import unittest

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestParticle))
    unittest.TextTestRunner(verbosity=2).run(suite)
