from interface_table import ITable


class OvalStoneTable(ITable):
    """
    Concrete implementation of OvalStoneTable
    """

    def __init__(self):
        self.width = 36
        self.length = 36

    def build_table(self):
        """

        :return: instance of SquareWoodenTable
        """
        return {
            "Oval_Stone_Table_top_only": f"width {self.width} inches and length{self.length} inches"
        }
