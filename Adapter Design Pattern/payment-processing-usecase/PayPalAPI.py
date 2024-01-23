class PayPalAPI:
    """PayPal API class working as a third party payment processor"""

    def __init__(self, api_key):
        self.api_key = api_key

    def paypal_payment(self, amount):
        print(f"Payment of {amount} made with PayPal")
        return True

    def paypal_refund(self, amount):
        print(f"Refund of {amount} made with PayPal")
        return True
