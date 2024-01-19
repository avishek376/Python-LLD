from abc import *


class IChair(ABC):
    """
    The chair interface to create chair implementations
    """

    @staticmethod
    @abstractmethod
    def get_chair_dimention():
        """
        :return: a chair instance with dimentions
        """
