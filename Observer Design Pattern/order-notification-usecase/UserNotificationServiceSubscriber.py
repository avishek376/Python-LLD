from OrderPlacedSubscriber import OrderPlacedSubscriber
from Amazon import Amazon


class UserNotificationService(OrderPlacedSubscriber):
    """This class represents the User Notification Subscriber"""

    def __init__(self) -> None:
        Amazon.add_subscriber(self)

    def on_order_placed(self, order_id: int):
        print(f"UserNotificationSubscriber: Notified of order id: {order_id}")
