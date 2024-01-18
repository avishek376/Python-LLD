from ShortChair import ShortChairImpl
from MediumChair import MediumChairImpl
from LargeChair import LargeChairImpl


class ChairFactory:
    """This is the Chair Factory Class"""

    @staticmethod
    def get_chair(chair_type):
        """This is the factory method"""
        try:
            if chair_type == "short-chair":
                return ShortChairImpl()
            elif chair_type == "medium-chair":
                return MediumChairImpl()
            elif chair_type == "large-chair":
                return LargeChairImpl()
            else:
                raise AttributeError("Chair Not Found")
            
        except Exception as _e:
            print(_e)
