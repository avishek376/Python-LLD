from abc import ABCMeta, abstractmethod


class IBuilder(metaclass=ABCMeta):
    """This interface provides Builder methods"""

    @staticmethod
    @abstractmethod
    def get_builder_a():
        pass

    @staticmethod
    @abstractmethod
    def get_builder_b():
        pass

    @staticmethod
    @abstractmethod
    def get_builder_c():
        pass

    @staticmethod
    @abstractmethod
    def get_product():
        pass
