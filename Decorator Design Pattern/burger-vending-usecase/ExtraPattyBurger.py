from BurgerDecorator import BurgerDecorator


class ExtraPattyBurger(BurgerDecorator):
    """This class is the Concrete implementation of BurgerDecorator"""

    def __init__(self, burger):
        super().__init__(burger)

    def get_cost(self):
        return super().get_cost() + 29

    def get_description(self):
        return f"{super().get_description()} with Extra Patty"
