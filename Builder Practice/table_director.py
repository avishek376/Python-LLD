from table_builder import TableBuilder


class TableDirector:
    """
    Concrete class representation for Table Director
    """

    @staticmethod
    def construct_product():
        return TableBuilder().set_top_base("Glass").set_bottom_legs(4).build_product()
