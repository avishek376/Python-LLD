class Table:
    """
    Concrete class representation of PRODUCT TABLE
    """

    def __init__(self, top_base: str = "Fibre", bottom_legs: int = 4) -> None:
        self.top_base = top_base
        self.bottom_legs = bottom_legs

    def construct(self):
        return f"A Table created with {self.top_base} top with {self.bottom_legs} legs"

