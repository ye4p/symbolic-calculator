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
        from .Expression import Expression
        return Expression([self, other])
    
    def __sub__(self, other):
        from .Expression import Expression
        return Expression([self, -other])
    
    def __mul__(self, other):
        from .Term import Term
        return Term(self, other)
    
    def __pow__(self, other):
        from .Power import Power
        return Power(self, other)

    def __truediv__(self, other):
        from .Power import Power
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

