from abc import ABC, abstractmethod

class Token(ABC):
    def __init__(self, position = None):
        self.position = position

    @classmethod
    @abstractmethod
    def construct(cls, lexer):
        pass

    @classmethod
    @abstractmethod
    def allowed(cls):
        pass
