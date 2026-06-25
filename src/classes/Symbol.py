from  src.classes.AlgebraicNode import AlgebraicNode, NodeType

# one of the base data types 
class Symbol(AlgebraicNode):  # for variables
    node_type= NodeType.SYMBOL
    def __init__(self, name):
        self.name = name       # will be a string storing the variables name
    def __repr__(self):
        return f"Symbol({self.name})"
    
    def __eq___(self, other):
        return self.name == other.name

    def simplify_symbol(self):
        return self
    
    def sort_key(self):
        return (self.node_type, self.name)