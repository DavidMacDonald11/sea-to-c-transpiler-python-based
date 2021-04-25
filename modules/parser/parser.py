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
        self.tokens += [self.token_stream.read(amount)]

    def take(self, amount = 1):
        taken = self.tokens[0:amount - 1]

        self.tokens = self.tokens[amount:]
        self.advance()

        return taken[0] if len(taken) == 0 else taken

    def make_ast(self):
        line = make_line_node(self, MAKE_COLLECTION)
