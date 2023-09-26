from impl_table_c import RoundGlassTable
from impl_table_b import SquareWoodenTable
from impl_table_a import OvalStoneTable


class TableFactory:
    """
        Factory class representation for TABLE
    """

    @staticmethod
    def get_table(table):
        """

        :param table: a table reference passed by client
        :return: a concrete table implementation
        """
        try:
            if table == "RoundGlassTable":
                return RoundGlassTable()
            elif table == "SquareWoodenTable":
                return SquareWoodenTable()
            elif table == "OvalStoneTable":
                return OvalStoneTable()

            raise Exception('Table Not Found')
        except Exception as _e:
            print(_e)

        return None
