from IProduct import IProduct


class ConcreteProductB(IProduct):
    """This class is the concrete implementation of product B"""

    def __init__(self):
        self.details = "Red colored product"

    def description(self):
        return f"Concrete Product B created a {self.details}"

