from abc import ABCMeta, abstractmethod


class IBuilder(metaclass=ABCMeta):
    """This interface provides Builder methods"""

    @staticmethod
    @abstractmethod
    def build_part_a():
        pass

    @staticmethod
    @abstractmethod
    def build_part_b():
        pass

    @staticmethod
    @abstractmethod
    def build_part_c():
        pass

    @staticmethod
    @abstractmethod
    def get_product():
        pass
