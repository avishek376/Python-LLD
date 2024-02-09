from ExtraCheeseBurger import ExtraCheeseBurger
from ExtraVeggieBurger import ExtraVeggieBurger
from ExtraPattyBurger import ExtraPattyBurger
from ConcreteBurgerComponent import BurgerComponent

if __name__ == "__main__":
    burger = BurgerComponent()
    extra_veggie_burger = ExtraVeggieBurger(burger)
    extra_cheese_burger = ExtraCheeseBurger(burger)
    mixed_burger = ExtraCheeseBurger(ExtraVeggieBurger(burger))

    print(burger.get_cost(), " | ", burger.get_description())
    print(extra_veggie_burger.get_cost(), " | ", extra_veggie_burger.get_description())
    print(extra_cheese_burger.get_cost(), " | ", extra_cheese_burger.get_description())
    print(mixed_burger.get_cost(), " | ", mixed_burger.get_description())

