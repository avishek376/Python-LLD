from abc import ABC, abstractmethod


class IFurnitureFactory(ABC):
    """
    Abstract Furniture Factory Interface
    """

    @staticmethod
    @abstractmethod
    def get_furniture():
        """

        :return: implement this method to return a furniture
        """
