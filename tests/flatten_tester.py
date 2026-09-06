from langparser import process
from src import AlgebraicNode, Expression, Term, Function, Symbol, Fraction

test_cases = ["3 + 4 + (2 + 2)", " 3 * 4 * (2*2)"]
answers = [
    Expression([Fraction(3),Fraction(4), Fraction(2), Fraction(2)]),
    Term([Fraction(3),Fraction(4), Fraction(2), Fraction(2)])
    ]

exprs = [process(t) for t in test_cases]

def test_flattening() -> bool:
    for i, e in enumerate(exprs):
        if e.flatten() != answers[i]:
            return False
    return True

assert(test_flattening())
print("Test passed on flattening")
