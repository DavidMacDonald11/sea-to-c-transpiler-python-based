import string
from .token import Token
from .keyword import Keyword

class Identifier(Token):
    def __init__(self, name, position = None):
        self.name = name
        super().__init__(position)

    def __repr__(self):
        return f"Identifier: {self.name}"

    @classmethod
    def construct(cls, lexer):
        token_string = lexer.take_while_allowed(cls.allowed())
        keyword = Keyword.get_keyword(token_string)

        if keyword is None:
            return Identifier(token_string)

        return Keyword(keyword)

    @classmethod
    def allowed(cls):
        return string.ascii_letters + "0123456789_"
