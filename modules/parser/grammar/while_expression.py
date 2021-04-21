from modules.lexer.token_types import TT
from .expression import make_expression
from ..nodes.collection import NODES

def make_while_expression(parser, **make_funcs):
    while_token = parser.take_token()
    condition = make_expression(parser, **make_funcs)

    parser.expecting(TT.COLON)
    expression = make_funcs["block_or_expression"](parser)

    return NODES.WhileNode(while_token, condition, expression)