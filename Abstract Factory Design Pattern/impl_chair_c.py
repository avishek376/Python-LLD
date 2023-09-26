from interface_chair import IChair


class SmallChair(IChair):
    """
    Implementation of small chair
    """

    def __init__(self):
        """
        constructor for chair instance to initialize
        """
        self.height = 40
        self.weight = 40
        self.width = 40
        self.material = "Plastic"

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
