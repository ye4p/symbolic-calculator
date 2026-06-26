from enum import IntEnum 
from src.classes.Expression import Expression
from src.classes.Term import Term
from src.classes.Power import Power

class AlgebraicNode:
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self):
        pass

    def __hash__(self):
        return hash(repr(self))

    def __add__(self, other):
        return Expression(self, other)
    
    def __sub__(self, other):
        return Expression(self, -other)
    
    def __mul__(self, other):
        return Term(self, other)
    
    def __pow__(self, other):
        return Power(self, other)

    def __truediv__(self, other):
        return Power(self, -other)

    def normalize(self):
        pass

    def simplify(self):
        pass

    def sub(self, symbol: str, value):
        pass # substitutes all occurences of certain symbol into the value
    
    def eval(self):
        pass # evaluates expression considering that there are no symbols

    def is_equal(self):
        pass
    
    def flatten(list):
        pass
    
    def sort_key(self):
        pass


class NodeType(IntEnum):
    SYMBOL=0
    FRACTION=1
    POWER=2
    TERM=3
    EXPRESSION=4
    FUNCTION=5
