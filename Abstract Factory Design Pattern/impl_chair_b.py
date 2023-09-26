from interface_chair import IChair


class MediumChair(IChair):
    """
    Implementation of medium chair
    """

    def __init__(self):
        self.height = 60
        self.width = 60
        self.weight = 60
        self.material = "Metal"

    def build_chair(self):
        """
            chair instance with criteria
            :return: a chair instance
            """
        return {
            "height": self.height,
            "weight": self.weight,
            "width": self.width,
            "Material used": self.material
        }
