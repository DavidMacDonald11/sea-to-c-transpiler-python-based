from enum import Enum, unique
from .token import Token

class Symbol(Token):
    def __init__(self, symbol, position = None):
        self.symbol = symbol
        super().__init__(position)

    def __repr__(self):
        return f"Symbol: {self.symbol.value}"

    @classmethod
    def construct(cls, lexer):
        symbol = Sym(lexer.take())

        if symbol is Sym.NEWLINE:
            lexer.at_line_start = True
            lexer.position.start.advance_line()

        return Symbol(symbol)

    @classmethod
    def allowed(cls):
        return {symbol.value for symbol in Sym}

@unique
class Sym(Enum):
    INDENT = "\t"
    NEWLINE = "\n"
    LPAREN = "("
    RPAREN = ")"
    COLON = ":"
    SEMICOLON = ";"
    EOF = ""
