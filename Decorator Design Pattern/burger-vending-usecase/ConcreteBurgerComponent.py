from Burger import Burger


class BurgerComponent(Burger):
    """This class is the default implementation of Burger interface"""

    def __init__(self):
        self._cost = 35
        self._description = "Burger"

    def get_cost(self):
        return self._cost

    def get_description(self):
        return self._description
