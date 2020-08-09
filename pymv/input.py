from pymv.ffcommand import ffcommand

class input(ffcommand):
    input_files = None

    def __init__(self):
        self.input_files = []

    def File(self, filename):
        pass