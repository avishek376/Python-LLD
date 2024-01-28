from abc import ABC, abstractmethod


class OrderPlacedSubscriber(ABC):
    """This class represents the Subscriber interface"""

    @abstractmethod
    def on_order_placed(self, order_id: int):
        pass
