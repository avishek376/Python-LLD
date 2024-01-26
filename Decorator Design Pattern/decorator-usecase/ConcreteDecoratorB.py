from BaseDecorator import Decorator


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        """
        Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.
        """
        return f"ConcreteDecoratorB({self.component.operation()})"
