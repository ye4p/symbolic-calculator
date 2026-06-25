from  src.classes.AlgebraicNode import AlgebraicNode, NodeType
import math

# One of the base datatypes
class Fraction(AlgebraicNode):
    node_type=NodeType.FRACTION
    def __init__(self, numerator, denominator=1):
        self.num = numerator
        self.den = denominator
        self.simplify_fraction()
    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"
    
    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def simplify_fraction(self):
        gcf = math.gcf(self.num, self.den)
        self.num//=gcf
        self.den//=gcf

        return self
    
    def simplify_fraction(self):
        return self.simplify_fraction()
    
    def sort_key(self):
        return (self.node_type, self.num/self.den)
    