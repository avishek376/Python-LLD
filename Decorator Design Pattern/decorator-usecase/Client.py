from ConcreteComponent import ConcreteComponent
from ConcreteDecoratorA import ConcreteDecoratorA

if __name__ == "__main__":
    # This way the client code can support both simple components...
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    print(simple.operation())
    print("\n")

    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    decorator1 = ConcreteDecoratorA(simple)

    print("Client: Now I've got a decorated component:")
    print(decorator1.operation())
    # print("\n")
    # decorator2.operation()
