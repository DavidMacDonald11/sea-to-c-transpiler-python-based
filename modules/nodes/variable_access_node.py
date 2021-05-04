from .ast_node import ASTNode

class VariableAccessNode(ASTNode):
    def __init__(self, identifier):
        self.identifier = identifier
        super().__init__(identifier.position)

    def __repr__(self):
        return f"{self.identifier}"

    def interpret(self, memory):
        pass

    def transpile(self, memory):
        pass
