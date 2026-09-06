from langparser import process
from src import AlgebraicNode, Expression, Term, Function, Symbol, Fraction

test_cases = ["x^2(1+ln(x))"]

exprs = [process(t) for t in test_cases]

def test_flattening():
    for i, e in enumerate(exprs):
        # print(e.flatten())
        e.flatten().pretty()

test_flattening()
