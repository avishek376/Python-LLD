from ITable import ITable


class NormalTable(ITable):
    """This is the NormalTable class which implements the ITable interface"""

    def __init__(self):
        self.top = "Fiber Top"
        self.legs = "Fiber Legs"

    def create(self):
        """This is the implementation of NormalTable create_table method"""
        return f"Normal table created using {self.top} and {self.legs}"
