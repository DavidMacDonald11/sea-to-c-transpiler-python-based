class Position:
    def __init__(self, file, start = None, end = None):
        self.file = file
        self.start = start
        self.end = end or start

    def __repr__(self):
        if self.start is None:
            return "Unknown Position"

        line = f"Line {self.start.line}"
        column = f"Col {self.start.column}"
        file = f"of {self.file}"

        if self.start.column != self.end.column:
            column += f" to {self.end.column}"

        if self.start.line != self.end.line:
            line += f" to {self.end.line}"

        return f"{line}, {column} {file}"

    def copy(self):
        positions = (self.start, self.end)
        positions = tuple(map(lambda x: x if x is None else x.copy(), positions))

        return Position(self.file, *positions)
