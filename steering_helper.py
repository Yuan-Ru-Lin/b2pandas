from anytree import NodeMixin, LevelOrderGroupIter
from functools import reduce

class BaseParticle:

    def __init__(self, name, variables):
        self.name = name
        self.variables = variables

class Particle(BaseParticle, NodeMixin):

    def __init__(self, name, variables, tex_code=None, parent=None, children=None):
        super(Particle, self).__init__(name=name, variables=variables)
        if tex_code:
            self.tex_code = tex_code
        self.parent = parent
        if children:
            self.children = children

    def __repr__(self):
        return f'{self.name}'

    def getVariable(self, variable, prefixed=False, parentheses=True):
        if prefixed:
            node = self
            string = variable
            while node.parent:
                string = Particle.daughter(string, node.parent.children.index(node))
                node = node.parent
            return string
        elif parentheses:
            return self.name + '_' + variable
        else:
            return self.name + '_' + variable.replace('(', '_').replace(')', '').replace(',', '_')
            

    def getVariables(self, prefixed=False, parentheses=True):
        return [self.getVariable(variable, prefixed=prefixed, parentheses=parentheses) for variable in self.variables]

    def getPredecessorsVariables(self, prefixed=False, parentheses=True):
        lst = []
        for children in LevelOrderGroupIter(self):
            for node in children:
                lst += node.getVariables(prefixed=prefixed, parentheses=parentheses)
        return lst

    @staticmethod
    def daughter(variable, order):
        return f"daughter({order},{variable})"


def concatenateCuts(cuts):
    if cuts:
        return ' and '.join(cuts)
    return ''

fourMomentum = ['E', 'px', 'py', 'pz']
metaData = ['__experiment__', '__run__', '__event__',  '__candidate__', '__ncandidates__', '__weight__']
