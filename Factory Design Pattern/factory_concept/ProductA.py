from IProduct import IProduct


class ConcreteProductA(IProduct):
    """This class is the concrete implementation of product A"""

    def __init__(self):
        self.details = "Green colored product"

    def description(self):
        return f"Concrete Product A created a {self.details}"
