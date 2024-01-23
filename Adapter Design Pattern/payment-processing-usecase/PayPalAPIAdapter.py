from PaymentAPIAdapter import PaymentAPIAdapter
from PayPalAPI import PayPalAPI


class PayPalAPIAdapter(PaymentAPIAdapter):
    """PayPal API Adapter class"""

    def __init__(self, api_key):
        self.paypal_api = PayPalAPI(api_key)

    def pay(self, amount):
        self.paypal_api.paypal_payment(amount)

    def refund(self, amount):
        self.paypal_api.paypal_refund(amount)

