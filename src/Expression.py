from .AlgebraicNode import AlgebraicNode
from .NodeType import NodeType
import langconfig

class Expression(AlgebraicNode): #Adding
    node_type=NodeType.EXPRESSION
    def __init__(self, terms):
        # self.consts = consts   # is a LIST of AlgebraicNodes
        # self.terms = terms.flatten()     # is a LIST of AlgebraicNodes
        self.terms = terms
    
    def __repr__(self):
        # return f"Expression({self.consts}, {self.terms})"
        return f"Expression({self.terms})"
    
    def __eq__(self, other):
        expr1 = self.normalize()
        expr2 = other.normalize()
        if (len(expr1.terms) != len(expr2.terms)):
            return False
        for i, f in enumerate(expr1.terms):
            if expr1.terms[i]!=expr2.terms[i]: 
                if langconfig.DEBUG:
                    print(f"Not equals: {expr1.terms[i]} and {expr2.terms[i]} at index {i}")
                    print(f"Result of comparison is: {expr1.terms[i]==expr2.terms[i]}")

                return False
        return True
    
    def __neg__(self):
        new_terms = [-el for el in self.terms]
        return Expression(new_terms)

    def flatten(self):
        flattened=self.flatten_helper(self.terms)
        return Expression(flattened)

    def flatten_helper(self, list):
        flattened=[]
        for el in list:
            if el.node_type==self.node_type:
                flattened+=self.flatten_helper(el.terms)
            else:
                flattened.append(el)
        return flattened

    def normalize(self):
        # Flatten expression
        flattened=self.flatten()

        if langconfig.DEBUG:
            self.type_check(flattened.terms)

        # Normalize:
        normalized_terms = [term.normalize() for term in flattened.terms]

        if langconfig.DEBUG:
            self.type_check(normalized_terms)


        # Sort:
        normalized_terms.sort(key = lambda node: node.sort_key())

        return Expression(normalized_terms)
    
    def simplify(self):
        from .Fraction import Fraction
        if len(self.terms)==1:
            return self.terms[0].simplify()

        normalized = self.terms.normalize()

        terms = [t.simplify() for t in normalized]
        
        filtered=[]
        for t in terms:
            if t == Fraction(0):
                continue
            filtered.append(t)

        # need to find common factors etc, such as 2x + 3x make it into 5x
        # 
        seen = []
        

        final = seen

        if len(final) == 1:
            return final[0]
        return Expression(final)
    
    def find_index(self, list, factor): # What is this ??
        for i, el in enumerate(list):
            if el.is_equal(factor):
                return 1
        return -1
    
    def sub(self, symbol, value):
        list1 = [el.sub(symbol, value) for el in self.terms]
        return Expression(list1)
    
    def eval(self):
        value = 0

        for el in self.terms:
            value+=el.eval()
        return value

    def eval_fraction_form(self):
        from .Fraction import Fraction
        value = Fraction(0)

        for el in self.terms:
            value+=el.eval_fraction_form()
        return value


    def sort_key(self):
        return (self.node_type, [t.sort_key() for t in self.terms] )
    
    def contains_symbol(self):
        for el in self.terms:
            if el.contains_symbol():
                return True
        return False

    def pretty(self, level: int = 0, comma: bool = False):
        print(level * langconfig.INDENTATION * " " + "Expression([")
        for term in self.terms[:-1]:
            term.pretty(level + 1, True)
        self.terms[-1].pretty(level+1)
        print(level * langconfig.INDENTATION * " "+"])" + ("," if comma else ""))
