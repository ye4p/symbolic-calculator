
class EvaluatingSymbolError(Exception):
    """Raised when trying to use eval() on a function that still has symbols in it"""
    pass

class UnknownMathFunctionCallError(Exception):
    """Raised when trying to call function that hasn't been added"""
    pass

class NotAlgebraicNodeClassType(Exception):
    """Raised if encountered None, int or some other object that isn't child of an AlgebraNode class"""
    pass