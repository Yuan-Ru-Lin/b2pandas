import unittest
from ..steering_helper import Particle


class TestParticle(unittest.TestCase):

    def setUp(self):
        self.commonVariables = ['mcPDG', 'isSignal']
        self.lambda0 = Particle(name="lambda0",
            variables=['nTracks', 'dr'] + self.commonVariables)
        self.proton = Particle(name="proton",
            variables=['protonID', 'charge'] + self.commonVariables,
            parent=self.lambda0)
        self.pion = Particle(name="pion",
            variables=['pionID', 'charge'] + self.commonVariables,
            parent=self.lambda0)

    def test_getVariablesPrefixed(self):
        """Check if the variables has been assigned"""
        self.assertEqual(self.lambda0.variables, ['nTracks', 'dr', 'mcPDG', 'isSignal'])
        self.assertEqual(self.proton.variables, ['protonID', 'charge', 'mcPDG', 'isSignal'])
        self.assertEqual(self.pion.variables, ['pionID', 'charge', 'mcPDG', 'isSignal'])
        self.assertEqual(self.lambda0.getAncestorsVariablesPrefixed(),
                         ['nTracks', 'dr', 'mcPDG', 'isSignal',
                          'daughter(0, protonID)', 'daughter(0, charge)',
                          'daughter(0, mcPDG)', 'daughter(0, isSignal)',
                          'daughter(1, pionID)', 'daughter(1, charge)',
                          'daughter(1, mcPDG)', 'daughter(1, isSignal)'])

    def tearDown(self):
        self.lambda0 = None
        self.proton = None
        self.pion = None
        self.commonVariables = None

if __name__ == '__main__':
    unittest.main()
