from OrderPlacedSubscriber import OrderPlacedSubscriber
from Amazon import Amazon


class SellerService(OrderPlacedSubscriber):
    """This class represents the Seller Subscriber"""

    def __init__(self):
        Amazon.add_subscriber(self)

    def on_order_placed(self, order_id: int):
        print(f"SellerSubscriber: Notified of order id: {order_id}")
