from .token import Token

class Identifier(Token):
    def __init__(self, name, position = None):
        self.name = name
        super().__init__(position)

    def __repr__(self):
        return f"Identifier: {self.name}"
