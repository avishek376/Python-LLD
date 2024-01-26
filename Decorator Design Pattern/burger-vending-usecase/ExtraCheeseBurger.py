from BurgerDecorator import BurgerDecorator


class ExtraCheeseBurger(BurgerDecorator):
    def __init__(self, burger):
        super().__init__(burger)

    def get_cost(self):
        return super().get_cost() + 10

    def get_description(self):
        return f"{super().get_description()}  with Extra Cheese"
