from enum import Enum, unique
from r_lexer import errors
from .token import Token

class Operator(Token):
    def __init__(self, operator, position = None):
        self.operator = operator
        super().__init__(position)

    def __repr__(self):
        return f"Operator: {self.operator.value}"

    @classmethod
    def construct(cls, lexer):
        token_string = lexer.take_while_allowed(cls.allowed())
        operator = cls.get_operator(token_string)

        return Operator(operator)

    @classmethod
    def get_operator(cls, token_string):
        for operator in Op:
            if token_string == operator.value:
                return operator

        raise errors.UnknownOperatorError(token_string)

    @classmethod
    def allowed(cls):
        return {c for c in op for op in Op}

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
