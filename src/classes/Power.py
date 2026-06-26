from  src.classes.AlgebraicNode import AlgebraicNode, NodeType
from src.classes.Fraction import Fraction
from src.classes.Term import Term

class Power(AlgebraicNode):
    node_type=NodeType.POWER
    def __init__(self, base, exp):
        self.base = base       # is a SINGLE AlgebraicNode
        self.exp = exp         # is a SINGLE AlgebraicNode
    def __repr__(self):
        return f"Power({self.base}, {self.exp})"
    
    def __eq__(self, other):
        return self.base == other.base and self.exp == other.exp

    def __neg__(self):
        return Term([-1, Power(self.base, self.exp)])

    def normalize(self):
        return Power(self.base.normalize(), self.exp.normalize())

    def simplify(self):
        base = self.base.simplify()
        exp = self.exp.simplify()
        
        if exp==0:
            return Fraction(1)
        if exp==1:
            return base
        else:
            return Power(base, exp)
        
    def sub(self, symbol, value):
        return Power(self.base.sub(symbol, value), self.exp.sub(symbol, value))

    def eval(self):
        val = self.base.eval() ** self.exp.eval()
        return val

    def sort_key(self):
        return (self.node_type, self.base.sort_key(), self.exp.sort_key())