from ConcreteVictorianTable import VictorianTable


class TableFactory:
    """This class is the Table Factory class"""

    def __init__(self):
        pass

    @staticmethod
    def get_table(table_type):
        """This is static Factory Method...return Table Factory Instances"""
        try:
            if table_type in ["victorian-table"]:
                return VictorianTable()
            elif table_type in ["modern-table"]:
                return None
            elif table_type in ["normal-table"]:
                return None
            raise ValueError("Table not found")
        except ValueError as e:
            print(e)
