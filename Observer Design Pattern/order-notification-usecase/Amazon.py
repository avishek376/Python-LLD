class Amazon:
    """This class represents the Publisher class"""
    _subscribers = []

    def __init__(self, order_id: int) -> None:
        self.order_id = order_id

    @staticmethod
    def add_subscriber(subscriber) -> None:
        Amazon._subscribers.append(subscriber)

    @staticmethod
    def remove_subscriber(subscriber) -> None:
        Amazon._subscribers.remove(subscriber)

    def notify_subscribers(self) -> None:
        for subscriber in Amazon._subscribers:
            subscriber.on_order_placed(self.order_id)

    def place_order(self) -> None:
        """This is the business logic method which uses the notify method to notify the subscribers"""
        print(f"Order with order id: {self.order_id} is placed")
        self.notify_subscribers()

