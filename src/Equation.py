from .AlgebraicNode import AlgebraicNode

class Equation(AlgebraicNode):
    def __init__(self, exprs):
        self.exprs=exprs