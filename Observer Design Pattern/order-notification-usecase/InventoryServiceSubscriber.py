from OrderPlacedSubscriber import OrderPlacedSubscriber
from Amazon import Amazon


class InventoryService(OrderPlacedSubscriber):
    """This class represents the Inventory Subscriber"""

    def __init__(self) -> None:
        Amazon.add_subscriber(self)

    def on_order_placed(self, order_id: int) -> None:
        print(f"InventorySubscriber: Notified of order id: {order_id}")
