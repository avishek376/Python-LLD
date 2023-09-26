from abc import ABC, abstractmethod


class ITable(ABC):
    """
    Table interface representation
    """

    @staticmethod
    @abstractmethod
    def build_table():
        """

        :return: impl class for building table
        """
