from UserNotificationServiceSubscriber import UserNotificationService
from InventoryServiceSubscriber import InventoryService
from SellerServiceSubscriber import SellerService
from Amazon import Amazon


class Client:
    amazon = Amazon(331928)
    user_notification_service = UserNotificationService()
    inventory_service = InventoryService()
    seller_service = SellerService()

    amazon.place_order()