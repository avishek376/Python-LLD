from interface_table import ITable


class RoundGlassTable(ITable):
    """
        Concrete class of RoundGlassTable
    """

    def __init__(self):
        self.diameter = 24
        self.thick = 8

    def build_table(self):
        """

        :return: instance of RoundGlassTable
        """
        return {
            "Round_Glass_Table_top_only": f"{self.diameter} inches diameter and {self.thick} mm thick"
        }
