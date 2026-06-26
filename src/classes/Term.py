from  src.classes.AlgebraicNode import AlgebraicNode, NodeType
from src.classes.Fraction import Fraction

class Term(AlgebraicNode): #Multiplication
    node_type=NodeType.TERM
    def __init__(self, factors):
        self.factors = factors.flatten() # is a LIST of AlgebraicNodes
    def __repr__(self):
        # return f"Term({self.coefs}, {self.factors})"
        return f"Term({self.factors})"
    
    def __eq__(self, other):
        term1 = self.normalize()
        term2 = other.normalize()
        if (len(term1.factors) != len(term2.factors)):
            return False
        for i, f in term1.factors:
            if term1.factors[i]!=term2.factors[i]: return False
        return True
    
    def __neg__(self):
        new_factors = [-el for el in self.factors]
        return Term(new_factors)

    def flatten(self, list):
        flattened=[]
        for el in list:
            if el.node_type==self.node_type:
                flattened+=self.flatten(el.factors)
            else:
                flattened.append(el)
        return flattened
    
    def normalize(self):
        # Flatten terms
        flattened=self.flatten(self.factors)

        # Normalize: 
        normalized = [factor.normalize() for factor in flattened]

        # Sort terms
        normalized.sort(key = lambda node: node.sort_key())

        return Term(normalized)


    def simplify(self):
        if len(self.factors) == 1:
            return self.factors[0].simplify()
        
        simplified = [f.simplify() for f in self.factors]
        filtered=[]

        for f in simplified:
            if f == Fraction(0):
                return Fraction(0)
            if f == Fraction(1):
                continue
            filtered.append(f)

        return Term(filtered)

    def sub(self, symbol, value):
        list1 = [el.sub(symbol, value) for el in self.factors]
        return Term(list1)
    
    def eval(self):
        value = 1

        for el in self.factors:
            # print("result of el.eval() on each factor in term is : ", el.eval())
            value*=el.eval()
        return value

    def sort_key(self):
        return (self.node_type, [f.sort_key() for f in self.factors] )