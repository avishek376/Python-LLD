from abc import ABC, abstractmethod


class ITable(ABC):
    """This is the common Abstract Class for Tables"""

    @abstractmethod
    def create(self):
        """This is the table method"""
        pass
