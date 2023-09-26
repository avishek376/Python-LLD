from abc import ABC, abstractmethod


class IChair(ABC):
    """
        Chair Interface representation
    """

    @staticmethod
    @abstractmethod
    def build_chair():
        """

        :return: impl class for building chair
        """
