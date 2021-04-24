from .token import Token

class Keyword(Token):
    def __init__(self, keyword, position = None):
        self.keyword = keyword
        super().__init__(position)

    def __repr__(self):
        return f"Keyword: {self.keyword}"

    @classmethod
    def construct(cls, lexer):
        return None

    @classmethod
    def get_keyword(cls, token_string):
        for keyword in KEYWORDS:
            if keyword == token_string:
                return keyword

        return None

    @classmethod
    def allowed(cls):
        return None

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
