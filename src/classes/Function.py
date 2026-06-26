import math
from  src.classes.AlgebraicNode import AlgebraicNode, NodeType
from src.lib.errors import UnknownMathFunctionCallError
FUNCTIONS={"sin", "cos", "tan", "ln", "log", "sqrt", "abs", "exp"}

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
    
    def sub(self, value):
        return Function(self.args.sub(value))
    
    def eval(self):
        args = self.args.eval()
        match self.func:
            case "sin":
                math.sin(args)
            case "cos":
                math.cos(args)
            case "tan":
                math.tan(args)
            case "ln":
                math.log(args)
            case "log":
                math.log10(args)
            case "abs":
                abs(args)
            case _:
                raise UnknownMathFunctionCallError(f"Unknown function: {self.func}")



    def sort_key(self):
        return (5, self.func, [a.sort_key() for a in self.args])