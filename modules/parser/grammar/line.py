from parser import errors
from position.position import Position
from tokens.symbol import Symbol, Sym
from tokens.keyword import Keyword
from nodes.eof_node import EOFNode
from nodes.line_node import LineNode

def make_line_node(parser, makes):
    if isinstance(parser.token, Symbol):
        if parser.token.symbol is Sym.EOF:
            return EOFNode(parser.take_and_advance())

        if parser.token.symbol is Sym.NEWLINE:
            parser.take_and_advance()
            return make_line_node(parser, makes)

    indent_start = parser.token.start
    parser.advance(parser.depth)
    indents = parser.take(parser.depth)

    has_indent = any(token.symbol is not Sym.INDENT for token in indents)
    non_indent_after = parser.token.symbol is not Sym.INDENT

    depth = count_indent(indents)
    indent_position = Position(indent_start, parser.token.position.end)

    if not has_indent or not non_indent_after:
        raise errors.IncorrectBlockError(depth, indent_position)

    return special_or_default(parser, makes)

def count_indent(indents):
    count = 0

    while isinstance(indents[count], Symbol) and indents[count].symbol is Sym.INDENT:
        count += 1

    return count

def special_or_default(parser, makes):
    if isinstance(parser.token, Keyword):
        special = {
            "pass": make_pass,
            "break": make_break_or_continue,
            "continue": make_break_or_continue,
            "do": make_do_while_expression,
            "while": make_while_expression,
            "for": make_for_expression,
            "if": make_if_expression
        }

        no_end = parser.token.keyword in special
        expression = special.get(parser.token.keyword, default)(parser, makes)
    else:
        no_end = False
        expression = default(parser, makes)

    return LineNode(expression, parser.depth, no_end)

def default(parser, makes):
    expression = makes.expression(parser, makes)

