from  src.classes.AlgebraicNode import AlgebraicNode, NodeType

class Term(AlgebraicNode): #Multiplication
    node_type=NodeType.TERM
    def __init__(self, factors):
        # self.coefs = coefs     # is a LIST of AlgebraicNodes
        self.factors = factors # is a LIST of AlgebraicNodes
    def __repr__(self):
        return f"Term({self.coefs}, {self.factors})"
    
    def __eq__(self, other):
        term1 = self.normalize()
        term2 = other.normalize()
        if (len(term1.factors) != len(term2.factors)):
            return False
        for i, f in term1.factors:
            if term1.factors[i]!=term2.factors[i]: return False
        return True

    
    def simplify_term(self):
        if len(self.factors) == 1:
            return self.factors[0].simplify()
        factors = [f.simplify() for f in self.factors]
        return Term(factors)
    
    def normalize_term(self):
        # Flatten terms
        flattened=self.flatten(self.factors)

        # Sort terms
        flattened.sort(key = lambda node: node.sort_key())

        return Term(flattened)

    def flatten(self, list):
        flattened=[]
        for el in list:
            if el.node_type==self.node_type:
                flattened+=self.flatten(el.factors)
            else:
                flattened.append(el)
        return flattened
    

    def sort_key(self):
        return (self.node_type, )