from langparser import process
from src import AlgebraicNode, Expression, Term, Power, Function, Symbol, Fraction
import sys

test_cases = ["3 + x + 3x + sin(x) + x^3 + (3+x)"]
answers = [
    Expression([Symbol("x"), Symbol("x"), Fraction(3.0, 1), Fraction(3.0, 1), Power(Symbol("x"), Fraction(3.0, 1)), Term([Symbol("x"), Fraction(3.0, 1)]), Function("sin", [Symbol("x")])])
    ]

expressions = [ process(tc) for tc in test_cases]

def test_normalize():
    for i, t in enumerate(expressions):
        normalized = t.normalize()
        if normalized != answers[i]:
            return False
    return True

assert(test_normalize())
print("Test passed on normalization")
