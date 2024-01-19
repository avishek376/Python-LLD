from ConcreteNormalChair import NormalChair
from ConcreteModernChair import ModernChair
from ConcreteVictorianChair import VictorianChair


class ChairFactory:
    """This is a Chair Factory class"""

    def __init__(self):
        pass

    @staticmethod
    def get_chair(chair_type):
        try:
            if chair_type == "modern-chair":
                return ModernChair()
            elif chair_type == "victoria-chair":
                return VictorianChair()
            elif chair_type == "normal-chair":
                return NormalChair()
            raise ValueError("Chair not found")

        except ValueError as e:
            print(e)
