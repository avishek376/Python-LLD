from IChair import IChair


class NormalChair(IChair):
    """This is the Concrete Class for Normal Chair"""

    def __init__(self):
        self.height = 2.0
        self.width = 1.5
        self.depth = 3.0

    def create(self):
        """This is the chair method"""
        return f"Normal chair created with dimensions: {self.height}x{self.width}x{self.depth}"
