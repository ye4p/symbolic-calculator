from .AlgebraicNode import AlgebraicNode
from .NodeType import NodeType
import langconfig

class Term(AlgebraicNode): #Multiplication
    node_type=NodeType.TERM
    def __init__(self, factors):
        # self.factors = factors.flatten() # is a LIST of AlgebraicNodes
        self.factors = factors
    def __repr__(self):
        # return f"Term({self.coefs}, {self.factors})"
        return f"Term({self.factors})"
    
    def __eq__(self, other):
        term1 = self.normalize()
        term2 = other.normalize()
        if (len(term1.factors) != len(term2.factors)):
            return False
        for i, f in enumerate(term1.factors):
            if term1.factors[i]!=term2.factors[i]:
                return False
        return True
    
    def __neg__(self):
        new_factors = [-el for el in self.factors]
        return Term(new_factors)

    def flatten(self):
        flattened=self.flatten_helper(self.factors)
        return Term(flattened)

    def flatten_helper(self, list):
        flattened=[]
        for el in list:
            if el.node_type==self.node_type:
                flattened+=self.flatten_helper(el.factors)
            else:
                flattened.append(el)
        return flattened
    
    def normalize(self):
        # Flatten terms
        flattened=self.flatten()

        # Normalize: 
        normalized = [factor.normalize() for factor in flattened.factors]

        # Sort terms
        normalized.sort(key = lambda node: node.sort_key())

        return Term(normalized)


    def simplify(self):
        from .Fraction import Fraction
        if len(self.factors) == 1:
            return self.factors[0].simplify()
        
        normalized = self.factors.normalize()

        simplified = [f.simplify() for f in normalized]
        filtered=[]

        for f in simplified:
            if f == Fraction(0):
                return Fraction(0)
            if f == Fraction(1):
                continue
            filtered.append(f)

        seen = []
        multiplier= Fraction(1)
        for f in filtered:
            if f.contains_symbol():
                seen.append(f)
                continue
            else:
                multiplier*=f
        if multiplier != Fraction(1):
            seen.append(multiplier)


        final = seen
        
        if len(final) == 1:
            return final[0]
        return Term(final)

    def sub(self, symbol, value):
        list1 = [el.sub(symbol, value) for el in self.factors]
        return Term(list1)
    
    def eval(self):
        value = 1

        for el in self.factors:
            # print("result of el.eval() on each factor in term is : ", el.eval())
            value*=el.eval()
        return value
    
    def eval_fraction_form(self):
        from .Fraction import Fraction
        value = Fraction(1)

        for el in self.factors:
            value *= el.eval_fraction_form()

        return value

    def sort_key(self):
        return (self.node_type, [f.sort_key() for f in self.factors] )
    
    def contains_symbol(self):
        for el in self.factors:
            if el.contains_symbol():
                return True
        return False

    def pretty(self, level: int = 0, comma: bool = False):
        print(level * langconfig.INDENTATION * " " + "Term([")
        for factor in self.factors[:-1]:
            factor.pretty(level + 1, True)
        self.factors[-1].pretty(level + 1)
        print(level * langconfig.INDENTATION * " "+"])" + ("," if comma else ""))