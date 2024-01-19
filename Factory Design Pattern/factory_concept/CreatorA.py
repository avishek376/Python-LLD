from Creator import Creator
from ProductA import ConcreteProductA


class ConcreteCreatorA(Creator):
    """This subclass provide the returns Product A"""

    def product_factory(self):
        return ConcreteProductA()
