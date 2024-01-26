from Creator import Creator
from ProductB import ConcreteProductB


class ConcreteCreatorB(Creator):
    """This class returns the Product B instance"""

    def product_factory(self):
        return ConcreteProductB()
