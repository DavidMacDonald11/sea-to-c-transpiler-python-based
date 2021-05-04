from parsing import errors
from tokens.symbol import Sym
from nodes.eof_node import EOFNode
from nodes.operations.sequential_node import SequentialOperationNode
from .makes import MAKES

class Parser:
    @property
    def tokens(self):
        return self.lexer.tokens

    @property
    def token(self):
        if self.i >= len(self.tokens):
            return self.tokens[-1]

        return self.tokens[self.i]

    @property
    def position(self):
        position = self.tokens[self.bounds[0]].position.copy()
        position.end = self.tokens[self.bounds[1]].position.end.copy()

        return position

    @property
    def indent(self):
        return [Sym.INDENT] * self.depth

    def __init__(self, lexer):
        self.lexer = lexer
        self.ast = None
        self.depth = 0
        self.i = 0
        self.bounds = [0, 0]

    def mark(self):
        self.bounds[1] = self.bounds[0] = self.i

    def advance(self, amount = 1):
        if amount < 1:
            return

        self.i += amount
        self.bounds[1] += amount

    def take(self, amount = 1):
        if amount < 1:
            return None

        i = self.i
        self.advance(amount)

        tokens = self.tokens[i:self.i] or [self.tokens[-1]]
        return tokens[0] if len(tokens) == 1 else tokens

    def retreat(self, amount = 1):
        if amount < 1:
            return

        self.i -= amount
        self.i = max(self.i, 0)

        self.bounds[1] = self.i
        self.bounds[0] = min(self.bounds)

    def expecting(self, *datas, check_type = False):
        for data in datas:
            if check_type:
                condition = isinstance(self.token, data)
            else:
                data_tuple = data if isinstance(data, (tuple, list)) else (data,)
                condition = self.token.data in data_tuple

            if not condition:
                raise errors.ExpectedTokenError(data)

            self.advance()

        self.retreat(len(datas))
        return self.take(len(datas))

    def wanting(self, *datas):
        try:
            bounds = self.bounds
            i = self.i

            return self.expecting(*datas)
        except errors.ExpectedTokenError:
            self.bounds = bounds
            self.i = i

            return None

    def make_ast(self):
        def make_node():
            line = MAKES.line(self, MAKES)

            if isinstance(line, EOFNode):
                return line

            return SequentialOperationNode(line, make_node())

        self.ast = make_node()