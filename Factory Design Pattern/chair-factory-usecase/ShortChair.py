from Chair import Chair


class ShortChairImpl(Chair):
    """This class is the ShortChair implementation of Chair"""

    def __init__(self):
        self.height = 2.0
        self.width = 1.5
        self.depth = 1.5

    def create_chair(self):
        """This is the implementation of ShortChair dimensions method"""
        return f"ShortChair created with dimensions: height: {self.height} width: {self.width} depth: {self.depth}"
