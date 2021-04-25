from errors.errors import SeaError

class ParserError(SeaError):
    parser = None

    def __init__(self, position = None, message = ""):
        if position is None:
            position = type(self).parser.token.position

        super().__init__(position, message)

class IncorrectBlockError(ParserError):
    def __init__(self, depth, position, message = ""):
        self.depth = depth
        self.expected = type(self).parser.depth
        super().__init__(position, message)

    def get_message(self):
        return f"Current block is {self.depth}, but expected block {self.expected}."
