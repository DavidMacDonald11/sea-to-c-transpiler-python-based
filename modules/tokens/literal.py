from lexer import errors
from .token import Token

class Literal(Token):
    def __init__(self, literal_type, value, position = None):
        self.type = literal_type
        self.value = value
        super().__init__(position)

    def __repr__(self):
        return f"Literal: {self.type} {self.value}"

    @classmethod
    def construct(cls, lexer):
        token_string = lexer.take_while_allowed(cls.allowed())
        dots = token_string.count(".")

        if dots > 1:
            raise errors.FloatError()

        if dots == 1:
            return Literal("float", token_string)

        return Literal("int", token_string)

    @classmethod
    def allowed(cls):
        return "0123456789."
