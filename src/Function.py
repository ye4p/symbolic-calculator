from .AlgebraicNode import AlgebraicNode
from .NodeType import NodeType
from lib.errors import UnknownMathFunctionCallError
import math

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
        from .Fraction import Fraction
        args = self.args.simplify()
        if not args.contains_symbol():
            ev = args.eval_fraction_form()
            if ev==Fraction(0) and self.func == "sin":
                return Fraction(0)
            # TODO add more
        return Function(self.func, args)
    
    def sub(self, value):
        return Function(self.func, self.args.sub(value))
    
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

    def eval_fraction_form(self):
        raise NotImplementedError

    def sort_key(self):
        return (5, self.func, [a.sort_key() for a in self.args])
    
    def contains_symbol(self):
        return self.args.contains_symbol()