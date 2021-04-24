from .token import Token

class Literal(Token):
    def __init__(self, literal_type, value, position = None):
        self.type = literal_type
        self.value = value
        super().__init__(position)

    def __repr__(self):
        return f"Literal: {self.type} {self.value}"
