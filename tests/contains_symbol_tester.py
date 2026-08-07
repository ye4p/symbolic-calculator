from langparser import process
from src import AlgebraicNode, Expression, Term, Function, Symbol, Fraction

test_cases = ["3/2 + 4*6 + sin(2) + 2^4", "3/2 + 4*x + sin(pi) + 2^4"]
answers = [
    False,
    True
    ]

exprs = [process(t) for t in test_cases]

def test_flattening() -> bool:
    for i, e in enumerate(exprs):
        if e.contains_symbol() != answers[i]:
            print(f"Test case {i+1}")
            return False
    return True

assert(test_flattening())
print("Test passed on contains_symbol method")

### NOTE! In the way it is, right now parser parser things like pi and it would count as symbol.