from ExtraCheeseBurger import ExtraCheeseBurger
from ExtraVeggieBurger import ExtraVeggieBurger
from ExtraPattyBurger import ExtraPattyBurger
from ConcreteBurgerComponent import BurgerComponent

if __name__ == "__main__":
    burger = BurgerComponent()
    extra_cheese_burger = ExtraCheeseBurger(burger)
    print(burger.get_cost())
    print(extra_cheese_burger.get_description())
    extra_veggie_burger = ExtraVeggieBurger(extra_cheese_burger)
    print(extra_veggie_burger.get_cost())
    print(extra_veggie_burger.get_description())
