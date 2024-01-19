from abc import abstractmethod, ABC


class ITableBuilder(ABC):
    """
    Interface representation for Table Builder Design Pattern
    """

    @staticmethod
    @abstractmethod
    def set_top_base():
        """
        setting the top base of product
        """

    @staticmethod
    @abstractmethod
    def set_bottom_legs():
        """
        setting up the bottom legs of product
        """

    @staticmethod
    @abstractmethod
    def build_product():
        """
        get the product after construction
        """
