from ITable import ITable


class ModernTable(ITable):
    """This is the ModernTable class which implements the ITable interface"""

    def __init__(self):
        self.top = "Glass Top"
        self.legs = "Steel Legs"

    def create(self):
        """This is the implementation of ModernTable create_table method"""
        return f"Modern table created using {self.top} and {self.legs}"
