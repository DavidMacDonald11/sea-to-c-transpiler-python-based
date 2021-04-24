from enum import Enum
from enum import unique
from .token import Token

class Symbol(Token):
    def __init__(self, symbol, position = None):
        self.symbol = symbol
        super().__init__(position)

    def __repr__(self):
        return f"Symbol: {self.symbol.value}"

@unique
class Sym(Enum):
    INDENT = ("\t", "    ")
    NEWLINE = "\n"
    LPAREN = "("
    RPAREN = ")"
    COLON = ":"
    SEMICOLON = ";"
    EOF = ""
