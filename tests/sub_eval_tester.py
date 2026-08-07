from langparser import process

test_cases = [ "2 + x", "8x", "3^x", "3"]
answers = [4, 16, 9, 3]

expressions =  [ process(tc) for tc in test_cases ]

def test_substitution_and_evaluation() -> bool:
    for i, el in enumerate(expressions):
        sub = el.sub("x", 2)
        val = sub.eval()
        print(f"got {val} and was supposed to get {answers[i]}")
        if val != answers[i]:
            return False
    return True

assert(test_substitution_and_evaluation())
print("Test passed on substitution and evaluation")