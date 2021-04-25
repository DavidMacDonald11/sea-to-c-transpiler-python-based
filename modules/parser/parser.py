from nodes.eof_node import EOFNode
from nodes.operations.sequential_node import SequentialOperationNode
from .make_collection import MAKE_COLLECTION
from .grammar.line import make_line_node

class Parser:
    @property
    def token(self):
        return self.tokens[0]

    def __init__(self, token_stream):
        self.token_stream = token_stream
        self.tokens = []
        self.depth = 0

        self.advance()

    def advance(self, amount = 1):
        if amount < 1:
            return

        self.tokens += [self.token_stream.read(amount)]

    def take(self, amount = 1):
        taken = self.tokens[0:amount - 1]
        self.tokens = self.tokens[amount:]

        return taken[0] if len(taken) == 1 else taken

    def take_and_advance(self, take_amount = 1, advance_amount = 1):
        taken = self.take(take_amount)
        self.advance(advance_amount)

        return taken

    def make_ast(self):
        line = make_line_node(self, MAKE_COLLECTION)

        if isinstance(line, EOFNode):
            return line

        return SequentialOperationNode(line, self.make_ast())
