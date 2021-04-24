class CharPosition:
    def __init__(self, line = 1, column = -1):
        self.line = line
        self.column = column

    def __eq__(self, position):
        return self.line == position.line and self.column == position.column

    def __repr__(self):
        return f"Line {self.line}, Col {self.column}"

    def copy(self):
        return CharPosition(self.line, self.column)

    def next(self):
        self.column += 1

    def next_line(self):
        self.line += 1
        self.column = -1
