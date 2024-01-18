from IChair import IChair


class VictorianChair(IChair):
    """This is the Concrete Class for Victorian Chair"""

    def __init__(self):
        self.height = 2.5
        self.width = 2.0
        self.depth = 4.0

    def create(self):
        """This is the chair method"""
        return f"Victorian chair created with dimensions: {self.height}x{self.width}x{self.depth}"
