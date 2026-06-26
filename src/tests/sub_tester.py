from src.parser.parser import Parser
from src.parser.lexer import Lexer

ex1="3.5x"
ex2="37x + x*2"

lexer= Lexer(ex1)
tokens=lexer.tokenize()
parser=Parser(tokens)

expr=parser.parse()

print(expr)

subsituted = expr.sub("x", 5)

print(subsituted)

val = subsituted.eval()

print(val)

