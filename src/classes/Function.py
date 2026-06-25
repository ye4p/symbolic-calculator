from  src.classes.AlgebraicNode import AlgebraicNode, NodeType

# this will be used for sin, cos, ln, etc.
class Function(AlgebraicNode):
    node_type = NodeType.FUNCTION
    def __init__(self, func, args):
        self.func = func       # will be a string like "sin" or "ln". can also be custom functions like "f" or "f_1"
        self.args = args       # is a LIST of AlgebraicNodes
    def __repr__(self):
        return f"FunctionCall({self.func}, {self.args})"
    
    def __eq__(self, other):
        expr1 = self.args.normalize()
        expr2 = other.args.normalize()
        return self.func == other.func and expr1 == expr2
    
    def simplify(self):
        args = self.args.simplify()
        return Function(self.func, args)
    
    def sort_key(self):
        return 0