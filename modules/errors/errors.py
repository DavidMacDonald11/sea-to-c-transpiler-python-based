class SeaError(Exception):
    def __init__(self, position = None, message = ""):
        self.message = message
        self.position = position
        super().__init__(message)

    def get_message(self):
        return self.message

    def get_position(self):
        return f"{self.position}"
