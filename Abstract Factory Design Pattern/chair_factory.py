from impl_chair_c import SmallChair
from impl_chair_b import MediumChair


class ChairFactory:
    """
    Factory class representation of CHAIR
    """

    @staticmethod
    def get_chair(chair):
        """

        :param chair: a chair reference passed by client
        :return: a concrete chair implementation
        """
        try:

            if chair == "SmallChair":
                return SmallChair()
            if chair == "MediumChair":
                return MediumChair()
            raise Exception("chair not found")
        except Exception as _e:
            print(_e)

        return None
