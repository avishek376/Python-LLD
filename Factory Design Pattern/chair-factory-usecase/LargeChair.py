from Chair import Chair


class LargeChairImpl(Chair):
    """This class is the Large Chair implementation of Chair"""

    def __init__(self):
        self.height = 4.0
        self.width = 3.0
        self.depth = 3.0

    def create_chair(self):
        """This is the implementation of LargeChair dimensions method"""
        return f"LargeChair created with dimensions: height: {self.height} width: {self.width} depth: {self.depth}"
