from ConcreteVictorianTable import VictorianTable
from ConcreteNormalTable import NormalTable
from ConcreteModernTable import ModernTable


class TableFactory:
    """This class is the Table Factory class"""

    def __init__(self):
        pass

    @staticmethod
    def get_table(table_type):
        """This is static Factory Method...return Table Factory Instances"""
        try:
            if table_type == "victorian-table":
                return VictorianTable()
            elif table_type == "modern-table":
                return ModernTable()
            elif table_type == "normal-table":
                return NormalTable()
            raise ValueError("Table not found")
        except ValueError as e:
            print(e)
