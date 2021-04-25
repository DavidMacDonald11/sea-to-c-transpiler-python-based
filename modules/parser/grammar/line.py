from tokens.symbol import Symbol, Sym

def make_line_node(parser, makes):
    if isinstance(parser.token, Symbol):
        if parser.token.symbol is Sym.EOF:
            pass