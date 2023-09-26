from abc import ABC

from interface_chair import IChair


class SmallChair(IChair, ABC):
    """
    small chair implementation
    """

    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    def get_chair_dimention(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }
