from  src.classes.AlgebraicNode import AlgebraicNode, NodeType
from src.classes.Fraction import Fraction

class Power(AlgebraicNode):
    node_type=NodeType.POWER
    def __init__(self, base, exp):
        self.base = base       # is a SINGLE AlgebraicNode
        self.exp = exp         # is a SINGLE AlgebraicNode
    def __repr__(self):
        return f"Power({self.base}, {self.exp})"
    
    def __eq__(self, other):
        return self.base == other.base and self.exp == other.exp

    def simplify_power(self):
        base = self.base
        exp = self.exp
        
        if exp==0:
            return Fraction(1)
        if exp==1:
            return base.simplify()
        else:
            return Power(base.simplify(), exp.simplify())

    def sort_key(self):
        #TODO
        return (self.node_type, )