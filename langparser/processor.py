from .token import Token
from .lexer import Lexer
from .parser import Parser

def process(str: str): # Returns fully parsed expression
    lexer = Lexer(str)

    tokens = lexer.tokenize()

    parser = Parser(tokens)

    res = parser.parse()

    return res