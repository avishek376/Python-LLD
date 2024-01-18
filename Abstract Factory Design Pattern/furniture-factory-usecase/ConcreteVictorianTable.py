from ITable import ITable


class VictorianTable(ITable):
    """This is the VictorianTable class which implements the ITable interface"""

    def __init__(self):
        self.top = "Wooden Top"
        self.legs = "Wooden Legs"

    def create(self):
        """This is the implementation of VictorianTable create_table method"""
        return f"Victorian table created using {self.top} and {self.legs}"
