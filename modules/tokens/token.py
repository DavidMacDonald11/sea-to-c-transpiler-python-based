from abc import ABC
from abc import abstractmethod

class Token(ABC):
    def __init__(self, position = None):
        self.position = position

    @abstractmethod
    def __repr__(self):
        pass
