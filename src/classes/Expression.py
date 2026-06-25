from  src.classes.AlgebraicNode import AlgebraicNode, NodeType


class Expression(AlgebraicNode): #Adding
    node_type=NodeType.EXPRESSION
    def __init__(self, terms):
        # self.consts = consts   # is a LIST of AlgebraicNodes
        self.terms = terms     # is a LIST of AlgebraicNodes
    def __repr__(self):
        return f"Expression({self.consts}, {self.terms})"
    
    def __eq__(self, other):
        expr1 = self.normalize()
        expr2 = other.normalize()
        if (len(expr1.terms) != len(expr2.terms)):
            return False
        for i, f in expr1.terms:
            if expr1.terms[i]!=expr2.terms[i]: return False
        return True

    def simplify_expression(self):
        if len(self.terms)==1:
            return self.terms[0].simplify()
        terms = [t.simplify() for t in self.terms]
        return Expression(terms)
    
    def normalize_expression(self):
        # first polynomials with descending order of their power
        # sort numerical values in descending order
        # skip the rest for now

        # Flatten expression
        flattened=self.flatten(self.terms)

        # Sort:
        flattened.sort(key = lambda node: node.sort_key())

        return Expression(flattened)

        
    
    def flatten(self, list):
        flattened=[]
        for el in list:
            if el.node_type==self.node_type:
                flattened+=self.flatten(el.terms)
            else:
                flattened.append(el)
        return flattened
        

    def sort_key(self):
        return (self.node_type, )