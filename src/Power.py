from  src.AlgebraicNode import AlgebraicNode, NodeType
from src.Fraction import Fraction
from src.Term import Term

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
        
        if exp==Fraction(0):
            return Fraction(1)
        elif exp==Fraction(1):
            return base
        elif base==Fraction(1):
            return Fraction(1)
        elif base==Fraction(0):
            return Fraction(0)
        elif not base.contains_symbol() and not exp.contains_symbol():
            base_frac = base.eval_fraction_form()
            exp_frac = exp.eval_fraction_form()
            return base_frac ** exp_frac
        elif isinstance(base, Power):
            return Power(base.base, base.exp * exp)
        # elif isinstance(base, Term):
        #     new = []
        #     for el in base.factors:
        #         new.append(Power(el, exp))
        #     return (Term(new))
        else:
            return Power(base, exp)
        
    def sub(self, symbol, value):
        return Power(self.base.sub(symbol, value), self.exp.sub(symbol, value))

    def eval(self):
        val = self.base.eval() ** self.exp.eval()
        return val
    
    def eval_fraction_form(self):
        val = self.base.eval_fraction_form() ** self.exp.eval_fraction_form()
        return val

    def sort_key(self):
        return (self.node_type, self.base.sort_key(), self.exp.sort_key())
    
    def contains_symbol(self):
        return self.base.contains_symbol() or self.exp.contains_symbol()