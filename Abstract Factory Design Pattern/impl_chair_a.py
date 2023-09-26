from interface_chair import IChair


class BigChair(IChair):
    """
    Implementation of big chair
    """

    def __init__(self):
        """
        constructor for chair instance to initialize
        """
        self.height = 80
        self.weight = 80
        self.width = 80
        self.material = "Metal with high durability"

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
