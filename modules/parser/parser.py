from modules.lexer.tokens import TT
from .nodes import NumberNode
from .nodes import BinaryOperationNode
from .nodes import UnaryOperationNode
from ..parser import errors

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_i = -1
        self.token = None
        self.advance()

    def take_token(self):
        token = self.token
        self.advance()
        return token

    def advance(self):
        self.token_i += 1

        if self.token_i < len(self.tokens):
            self.token = self.tokens[self.token_i]

        return self.token

    def parse(self):
        return self.expression()

    def factor(self):
        if self.token.type in (TT.PLUS, TT.MINUS):
            operation_token = self.take_token()
            return UnaryOperationNode(operation_token, self.factor())
        elif self.token.type in (TT.INT, TT.FLOAT):
            return NumberNode(self.take_token())
        elif self.token.type == TT.LPAREN:
            self.advance()
            node = self.expression()

            if self.token.type == TT.RPAREN:
                self.advance()
                return node

            raise errors.NoClosingParenthesisError(self.token)

        raise errors.FactorError(self.token)

    def term(self):
        return self.binary_operation(self.factor, (TT.STAR, TT.SLASH))

    def expression(self):
        return self.binary_operation(self.term, (TT.PLUS, TT.MINUS))

    def binary_operation(self, func, operations):
        left = func()

        while self.token.type in operations:
            operation_token = self.take_token()
            right = func()
            left = BinaryOperationNode(left, operation_token, right)

        return left