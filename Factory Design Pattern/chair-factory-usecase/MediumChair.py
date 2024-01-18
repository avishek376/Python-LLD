from Chair import Chair


class MediumChairImpl(Chair):
    """This class is the MediumChair implementation of Chair"""

    def __init__(self):
        self.height = 3.0
        self.width = 2.0
        self.depth = 2.0

    def create_chair(self):
        """This is the implementation of MediumChair dimensions method"""
        return f"MediumChair created with dimensions: height: {self.height} width: {self.width} depth: {self.depth}"
