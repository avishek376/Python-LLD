from abc import ABC, abstractmethod


class IDialog(ABC):
    """This class is the Creator class"""

    @abstractmethod
    def factory(self):
        """Providing the factory method"""
        pass

    @staticmethod
    def business_logic():
        print("business logic")
