from interface_chair import IChair


class MediumChair(IChair):
    """
    medium chair implementation
    """

    def __init__(self):
        self._height = 60
        self._width = 60
        self._depth = 60

    def get_chair_dimention(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }
