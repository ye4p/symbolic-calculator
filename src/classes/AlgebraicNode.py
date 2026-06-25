from enum import Enum

class AlgebraicNode:
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self):
        pass
    
    def normalize(self):
        self.normalize_expression()

    def simplify(self):
        self.simplify_expression()
    
    def simplify_expression(self):
        pass
    
    def is_equal(self):
        pass
    
    def flatten(list):
        pass
    
    def sort_key(self):
        pass


class NodeType(Enum):
    SYMBOL=0
    FRACTION=1
    POWER=2
    TERM=3
    EXPRESSION=4
    FUNCTION=5
