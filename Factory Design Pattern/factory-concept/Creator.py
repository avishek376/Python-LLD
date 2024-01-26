from abc import ABC, abstractmethod


class Creator(ABC):
    """This is a creator class"""

    @staticmethod
    @abstractmethod
    def product_factory():
        """This is the factory method"""
        pass

    def business_logic(self):
        """this is a business logic method which uses factory method"""

        product = self.product_factory()
        return product.description()
