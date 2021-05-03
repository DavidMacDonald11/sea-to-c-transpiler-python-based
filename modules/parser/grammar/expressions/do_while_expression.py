from tokens.symbol import Sym
from nodes.expressions.do_while_node import DoWhileNode

def make_do_while_expression(parser, makes):
    do_token = parser.take()
    parser.expecting(Sym.COLON)

    block = makes.block_or_expression(parser, makes)
    else_case = None

    parser.expecting(parser.indent, "while")
    condition = makes.expression(parser, makes)

    if parser.wanting("else") is not None:
        parser.expecting(Sym.COLON)
        else_case = makes.block_or_expression(parser, makes)
    else:
        parser.expecting((Sym.NEWLINE, Sym.EOF))
        parser.grab_newlines()

        if parser.wanting(parser.indent, "else") is not None:
            parser.expecting(Sym.COLON)
            else_case = makes.block_or_expression(parser, makes)

    return DoWhileNode(do_token, block, condition, else_case)
