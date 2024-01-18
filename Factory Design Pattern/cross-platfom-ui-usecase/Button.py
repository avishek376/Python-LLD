from abc import ABC, abstractmethod


class IButton(ABC):
    """This is the product interface"""

    @abstractmethod
    def click(self, category):
        """this method provide IoS/Windows implementations"""
        pass


