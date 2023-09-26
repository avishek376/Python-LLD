from interface_table import ITable


class SquareWoodenTable(ITable):
    """
    Concrete class of SquareWoodenTable
    """

    def __init__(self):
        self.width = 36
        self.length = 36

    def build_table(self):
        """

        :return: instance of SquareWoodenTable
        """
        return {
            "Square_Wooden_Table_top_only": f"width {self.width} inches and length{self.length} inches"
        }
