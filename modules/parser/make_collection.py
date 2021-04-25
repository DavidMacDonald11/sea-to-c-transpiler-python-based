from types import SimpleNamespace
from .grammar.line import make_line_node

MAKE_COLLECTION = SimpleNamespace(
    line_node = make_line_node
)
