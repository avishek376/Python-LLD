from Burger import Burger


class BurgerDecorator(Burger):
    """"This class is the Base Decorator of Burger interface"""

    def __init__(self, burger):
        self._burger = burger

    def get_cost(self):
        return self._burger.get_cost()

    def get_description(self):
        return self._burger.get_description()

    