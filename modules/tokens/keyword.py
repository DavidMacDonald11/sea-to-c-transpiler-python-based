from .token import Token

class Keyword(Token):
    def __init__(self, keyword, position = None):
        self.keyword = keyword
        super().__init__(position)

    def __repr__(self):
        return f"Keyword: {self.keyword}"

TYPE_KEYWORDS = { "int", "float", "bool" }
BOOL_KEYWORDS = { "not", "and", "or" }

SYNTAX_KEYWORDS = {
    "if",
    "elif",
    "else",
    "for",
    "while",
    "do",
    "break",
    "continue",
    "pass"
}

KEYWORDS = TYPE_KEYWORDS | BOOL_KEYWORDS | SYNTAX_KEYWORDS
