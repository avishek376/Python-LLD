from abc import ABC, abstractmethod


class IFurniture(ABC):
    """This class is the common Abstract Class for Furniture"""

    @staticmethod
    @abstractmethod
    def get_furniture(furniture_type):
        """This is the furniture method"""
        pass
