from enum import Enum
from enum import unique
from .token import Token

class Operator(Token):
    def __init__(self, operator, position = None):
        self.operator = operator
        super().__init__(position)

    def __repr__(self):
        return f"Operator: {self.operator.value}"

@unique
class Op(Enum):
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    POWER = "**"
    DIVIDE = "/"
    MODULO = "%"
    NOT = "~"
    LSHIFT = "<<"
    RSHIFT = ">>"
    AND = "&"
    XOR = "^"
    OR = "|"

    EQUALS = "="
    PLUS_EQUALS = "+="
    INCREMENT = "++"
    MINUS_EQUALS = "-="
    DECREMENT = "--"
    MULTIPLY_EQUALS = "*="
    POWER_EQUALS = "**="
    DIVIDE_EQUALS = "/="
    MODULO_EQUALS = "%="
    LSHIFT_EQUALS = "<<="
    RSHIFT_EQUALS = ">>="
    AND_EQUALS = "&="
    XOR_EQUALS = "^="
    OR_EQUALS = "|="

    EQ = "=="
    NE = "!="
    LT = "<"
    GT = ">"
    LTE = "<="
    GTE = ">="
