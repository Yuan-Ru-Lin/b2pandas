import unittest
from ..steering_helper import Decay, Node


class TestDecay(unittest.TestCase):

    def setUp(self):
        self.lambda0 = Node(symbol="Lambda0", name="Lambda0")
        self.proton = Node(symbol="p", name="proton")
        self.pion = Node(symbol="pi-", name="pion")
        self.commonVariables = ['M', 'PDG', 'mcPDG', 'isSignal', ]
        self.my_decay = Decay(self.lambda0)

    def test_add_daughter(self):
        self.lambda0.add_daughter(self.proton)
        self.lambda0.add_daughter(self.pion)
        self.assertEqual(self.lambda0.daughters[0], self.proton)
        self.assertEqual(self.lambda0.daughters[1], self.pion)

    def test_add_variables(self):
        self.lambda0.add_variables(['nTracks', 'dr', 'chiProb',
                                    'cosAngleBetweenMomentumAndVertexVector', ] + self.commonVariables)
        self.proton.add_variables(['protonID', 'charge', 'clusterE', 'clusterHighestE',
                                   'clusterE1E9', 'clusterE9E21', 'clusterNHits', ] + self.commonVariables)
        self.pion.add_variables(['pionID', 'charge', ] + self.commonVariables)
        print(self.my_decay.translate_variables_for_BASF2())

    def tearDown(self):
        self.lambda0 = None
        self.proton = None
        self.pion = None
        self.commonVariables = None
        self.my_decay = None

if __name__ == '__main__':
    unittest.main()
