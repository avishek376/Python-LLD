from CreatorA import ConcreteCreatorA
from CreatorB import ConcreteCreatorB


class Client:
    print(ConcreteCreatorA().business_logic())

    print(ConcreteCreatorB().business_logic())
