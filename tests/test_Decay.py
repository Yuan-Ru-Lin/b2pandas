import unittest
from ..steering_helper import Decay, Node


class TestDecay(unittest.TestCase):

    def setUp(self):
        self.lambda0 = Node(symbol="Lambda0", name="Lambda0")
        self.proton = Node(symbol="p", name="proton")
        self.pion = Node(symbol="pi-", name="pion")
        self.commonVariables = ['mcPDG', 'isSignal']
        self.my_decay = Decay(self.lambda0)
        self.lambda0.add_daughter(self.proton)
        self.lambda0.add_daughter(self.pion)

    def test_add_daughter(self):
        """Check if the daughters has been linked to the mother mutually"""
        self.assertEqual(self.lambda0.daughters[0], self.proton)
        self.assertEqual(self.lambda0.daughters[1], self.pion)
        self.assertEqual(self.proton.mother, self.lambda0)
        self.assertEqual(self.pion.mother, self.lambda0)

    def test_add_variables(self):
        self.lambda0.add_variables(['nTracks', 'dr'] + self.commonVariables)
        self.proton.add_variables(['protonID', 'charge'] + self.commonVariables)
        self.pion.add_variables(['pionID', 'charge'] + self.commonVariables)

        # Check if the variables has been assigned
        self.assertEqual(self.lambda0.variables, ['nTracks', 'dr', 'mcPDG', 'isSignal'])
        self.assertEqual(self.proton.variables, ['protonID', 'charge', 'mcPDG', 'isSignal'])
        self.assertEqual(self.pion.variables, ['pionID', 'charge', 'mcPDG', 'isSignal'])
        self.assertEqual(self.my_decay.translate_variables_for_BASF2(),
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
        self.my_decay = None

if __name__ == '__main__':
    unittest.main()
