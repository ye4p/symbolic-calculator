from  src.classes.AlgebraicNode import AlgebraicNode, NodeType
import math
from fractions import Fraction as PyFraction

# One of the base datatypes
class Fraction(AlgebraicNode):
    node_type=NodeType.FRACTION
    def __init__(self, numerator, denominator=1):
        self.num = numerator
        self.den = denominator
        # self.simplify_fraction()
    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"
    
    def __eq__(self, other):
        return self.num == other.num and self.den == other.den
    
    def __neg__(self):
        return Fraction(-1*self.num, self.den)

    def normalize(self):
        return self
    # def simplify_fraction(self):
    #     num = int(self.num)
    #     den = int(self.den)
    #     gcd = math.gcd(num, den)
    #     num//=gcd
    #     den//=gcd
    #     x = Fraction(self.num,)

    #     return Fraction(str(num), str(den))

    def simplify(self):
        return self

    def sub(self, symbol, value):
        return self
    
    def eval(self):
        # print("result of fraction eval is: ", self.num / self.den)
        return self.num / self.den
    
    
    def sort_key(self):
        return (self.node_type, self.num/self.den)
    