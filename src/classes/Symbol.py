from  src.classes.AlgebraicNode import AlgebraicNode, NodeType
from src.classes.Fraction import Fraction
from src.lib.errors import EvaluatingSymbolError
from src.classes.Term import Term

# one of the base data types 
class Symbol(AlgebraicNode):  # for variables
    node_type= NodeType.SYMBOL
    def __init__(self, name):
        self.name = name       # will be a string storing the variables name
    def __repr__(self):
        return f"Symbol({self.name})"
    
    def __eq___(self, other):
        return self.name == other.name
    
    def __neg__(self):
        return Term([Fraction(-1), self])

    def normalize(self):
        return self

    def simplify_symbol(self):
        return self
    
    def sub(self, symbol, value):
        if (symbol == self.name):
            return Fraction(value)
        else:
            return self
    
    def eval(self):
        raise EvaluatingSymbolError(f"Can't evaluate symbol {self.name}")

    def sort_key(self):
        return (self.node_type, self.name)