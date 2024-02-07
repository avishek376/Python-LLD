from IFurniture import IFurniture
from ConcreteChairFactory import ChairFactory
from ConcreteTableFactory import TableFactory


class FurnitureFactory(IFurniture):
    """This is the Abstract Furniture Factory class"""

    @staticmethod
    def get_furniture(furniture_type):
        """This is static Factory Method...return Furniture Factory Instances"""
        try:
            if furniture_type in ["modern-chair", "victorian-chair", "normal-chair"]:
                return ChairFactory().get_chair(furniture_type)
            elif furniture_type in ["modern-table", "victorian-table", "normal-table"]:
                return TableFactory().get_table(furniture_type)

            raise ValueError("Furniture not found")
        except ValueError as e:
            print(e)
