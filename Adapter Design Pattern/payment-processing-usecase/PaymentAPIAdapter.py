from abc import ABC, abstractmethod


class PaymentAPIAdapter(ABC):
    """Abstract class for Payment API Adapter"""

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass
