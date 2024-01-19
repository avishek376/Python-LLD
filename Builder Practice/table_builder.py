from table_product import Table
from interface_table_builder import ITableBuilder


class TableBuilder(ITableBuilder):
    """
    Builder Design Pattern class of Table
    """

    def __init__(self):
        self.table = Table()

    def set_top_base(self, top_base):
        self.table.top_base = top_base
        return self

    def set_bottom_legs(self, bottom_legs):
        self.table.bottom_legs = bottom_legs
        return self

    def build_product(self):
        return self.table
