from abc import ABC, abstractmethod


class IChair(ABC):
    """This is the common Abstract Class for Chairs"""

    @staticmethod
    @abstractmethod
    def create(self):
        """This is the chair method"""
        pass
