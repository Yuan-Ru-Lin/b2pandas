from anytree import NodeMixin, LevelOrderGroupIter

class BaseParticle:

    def __init__(self, name, variables):
        self.name = name
        self.variables = variables

class Particle(BaseParticle, NodeMixin):

    def __init__(self, name, variables, parent=None, children=None):
        super(Particle, self).__init__(name=name, variables=variables)
        self.parent = parent
        if children:
            self.children = children

    def getVariablePrefixed(self, variable):
        node = self
        string = variable
        while node.parent:
            string = Particle.daughter(string, node.parent.children.index(node))
            node = node.parent
        return string

    def getVariablesPrefixed(self):
        return [self.getVariablePrefixed(variable) for variable in self.variables]

    def getAncestorsVariablesPrefixed(self):
        lst = []
        for children in LevelOrderGroupIter(self):
            for node in children:
                lst += node.getVariablesPrefixed()
        return lst

    @staticmethod
    def daughter(variable, order):
        return f"daughter({order}, {variable})"


fourMomentum = ['E', 'px', 'py', 'pz']
metaData = ['__experiment__', '__run__', '__event__',  '__candidate__', '__ncandidates__', '__weight__']
