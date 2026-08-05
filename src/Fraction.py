from .AlgebraicNode import AlgebraicNode
from .NodeType import NodeType
from fractions import Fraction as PyFraction 
import math
import langconfig

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
    
    def __add__(self, other):
        from .Expression import Expression
        if not other.contains_symbol():
            evaluated = other.eval_fraction_form()
            new_den = self.den * evaluated.den
            num1 = self.num * evaluated.den
            num2 = evaluated.num * self.den

            return Fraction(num1 + num2, new_den).simplify_fraction()
        return Expression(self, other).flatten()
        
    def __sub__(self, other):
        return self + (-other)
    
    def __mul__(self, other):
        from .Term import Term
        if not other.contains_symbol():
            ev = other.eval_fraction_form()
            return Fraction(self.num*ev.num, self.den*ev.den).simplify_fraction()
        return Term(self, other).flatten()
    
    def __truediv__(self, other):
        from .Power import Power
        from .Term import Term
        if not other.contains_symbol():
            ev = other.eval_fraction_form()
            return Fraction(self.num * ev.den, self.den * ev.num)
        return Term([self, Power(other, -1)]).flatten()

    def __pow__(self, other):
        from .Power import Power
        if not other.contains_symbol():
            ev = other.eval_fraction_form()
            if ev.den == 1:
                return Fraction(self.num ** ev.num, self.den ** ev.num)
            if (self.num ** ev.den).is_integer() and (self.den ** ev.den).is_integer():
                return Fraction(self.num ** (ev.num/ev.den), self.den ** (ev.num/ev.den))
        return Power(self, other)

    def normalize(self):
        return self
    
    def simplify_fraction(self):
        num = int(self.num)
        den = int(self.den)
        gcd = math.gcd(num, den)
        num//=gcd
        den//=gcd

        if den < 0:
            den = -den
            num = -num
        return Fraction(num, den)

    def simplify(self):
        return self.simplify_fraction()

    def sub(self, symbol, value):
        return self
    
    def eval(self):
        # print("result of fraction eval is: ", self.num / self.den)
        return self.num / self.den
    
    def eval_fraction_form(self):
        return self.simplify_fraction()
    
    
    def sort_key(self):
        return (self.node_type, self.num/self.den)
    
    def contains_symbol(self):
        return False

    def pretty(self, level: int = 0, comma: bool = False):
        print(level * langconfig.INDENTATION * " " + f"Fraction({self.num}, {self.den})" + ("," if comma else ""))
    