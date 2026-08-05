from langparser.parser import Parser, Lexer

ex1="3.5x"
ex2="37x + x*2"

lexer= Lexer(ex1)
tokens=lexer.tokenize()
parser=Parser(tokens)

expr=parser.parse()

print(expr)

norm = expr.normalize()

print(norm)