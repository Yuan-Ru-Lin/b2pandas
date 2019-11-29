class Node():

    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
        self.mother = None
        self.daughters = []
        self.variables = []

    def __str__(self):
        return f'{self.name} ({self.symbol}) -> {self.daughters}; variables: {self.variables}'

    def __repr__(self):
        particle_string = f'{self.name} ({self.symbol})'
        if self.daughters:
            particle_string += f' -> {self.daughters}'
        return particle_string

    def add_variables(self, variables):
        self.variables += variables

    def add_daughter(self, daughter_node):
        self.daughters.append(daughter_node)
        self.daughters[-1].mother = self

    def rank(self):
        assert self.mother, "This node has no mother!"
        return self.mother.daughters.index(self)

    def own(self, variable):
        if self.mother:
            daughter_order = self.rank()
            return variable[:21] == "daughter__bo" + str(daughter_order) + "__cm__sp"
        else:
            return variable in self.variables

    def distribute_variables_to_daughters(self):
        for daughter in self.daughters:
            for variable in self.variables:
                if daughter.own(variable):
                    daughter.variables.append(variable)
                    self.variables.remove(variable)

    def rename_every_own_variables(self):
        renamed_variables = []
        for variable in self.variables:
            renamed_variables.append(no_parentheses(variable))
        self.variables = renamed_variables


class Decay():

    def __init__(self, mother: Node):
        self.mother = mother

    def rename_every(self, variables):
        self.mother.variables = variables
        self.mother.distribute_variables_to_daughters()
        self.mother.rename_every_own_variables()
        for daughter in self.mother.daughters:
            daughter.rename_every_own_variables()

    def translate_variables_for_BASF2(self):
        basf2_variables = []
        basf2_variables += self.mother.variables
        for daughter in self.mother.daughters:
            basf2_variables += map(lambda var: 'daughter(' +
                                   str(daughter.rank()) + ', ' + var + ')', daughter.variables)
        return basf2_variables

    def get_variables(self):
        variables_to_print = []
        variables_to_print += self.mother.variables
        for daughter in self.mother.daughters:
            variables_to_print += map(lambda var: daughter.name +
                                      "_" + var, daughter.variables)
        return variables_to_print


def no_parentheses(var):
    if "daughter__bo" in var:
        return var[21:-4]
    else:
        return var


fourMomentum = ['E', 'px', 'py', 'pz']
