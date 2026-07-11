from enum import IntEnum 
from src.Expression import Expression
from src.Term import Term
from src.Power import Power
from src.Fraction import Fraction

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
    
    def eval(self) -> float:
        pass # evaluates expression considering that there are no symbols
    
    def eval_fraction_form(self) -> Fraction:
        pass # evaluates expression into fraction form to keep precision

    def is_equal(self, other):
        return self == other # for now its fine but later will need to change
    
    def flatten(self, list):
        pass
    
    def sort_key(self):
        pass

    def contains_symbol(self) -> bool:
        pass


class NodeType(IntEnum):
    SYMBOL=0
    FRACTION=1
    POWER=2
    TERM=3
    EXPRESSION=4
    FUNCTION=5
