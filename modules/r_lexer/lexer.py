from position.position import Position
from tokens.identifier import Identifier
from tokens.operator import Operator
from tokens.symbol import Symbol, Sym
from tokens.literal import Literal
from r_lexer import errors

class Lexer:
    @property
    def symbol(self):
        return self.symbols[0]

    def __init__(self, input_stream):
        self.input_stream = input_stream
        self.position = Position(input_stream)

        self.at_line_start = True
        self.symbols = ""

        self.advance()

    def advance(self, amount = 1):
        self.symbols += "".join(self.input_stream.read(amount))

    def take(self, amount = 1):
        taken = self.symbols[0:amount - 1]

        self.symbols = self.symbols[amount:]
        self.position.start.advance(amount)

        self.advance()
        return taken

    def take_while_allowed(self, allowed):
        token_string = ""

        while self.symbol in allowed:
            token_string += self.take()

        return token_string

    def make_tokens(self):
        return list(self.generate_tokens()) + [Symbol(Sym.EOF, self.position.copy())]

    def generate_tokens(self):
        while self.symbols != "":
            self.check_for_spaces()

            position = self.position.copy()
            token = self.construct_token()
            position.end = self.position.start.copy()
            token.position = position

            yield token

    def check_for_spaces(self):
        is_space = self.symbol == " "
        is_tab = self.symbol == "\t"
        at_start = self.at_line_start

        if not at_start and (is_space or is_tab):
            self.take()
            return

        if at_start and not is_space and not is_tab:
            self.at_line_start = False
            return

        if at_start and is_space:
            self.advance(3)

            if self.symbols != " " * 4:
                raise errors.IndentError()

            self.symbols = "\t"

    def construct_token(self):
        for token_type in {Symbol, Operator, Literal, Identifier}:
            if self.symbol in token_type.allowed():
                return token_type.construct(self)

        raise errors.UnknownSymbolError(self.symbol)
