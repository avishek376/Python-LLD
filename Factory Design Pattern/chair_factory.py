from impl_small_chair import SmallChair
from impl_medium_chair import MediumChair


class ChairFactory:
    """
    chair factory class to provide chairs based on requirement
    """

    @staticmethod
    def get_chair(chair):
        if chair == "SmallChair":
            return SmallChair()
        if chair == "MediumChair":
            return MediumChair()

        return None
