from ChairFactory import ChairFactory


class Client:
    """This is the Client Class"""

    chair = ChairFactory.get_chair("medium-chair")
    print(chair.create_chair())
