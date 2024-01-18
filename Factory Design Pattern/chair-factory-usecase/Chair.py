from abc import ABC, abstractmethod


class Chair(ABC):
    """This is the common Abstract Class for Chair Components"""

    @staticmethod
    @abstractmethod
    def create_chair():
        """This is the chair method"""
        pass
