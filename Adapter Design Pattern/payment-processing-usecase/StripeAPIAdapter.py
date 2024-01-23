from PaymentAPIAdapter import PaymentAPIAdapter
from StripeAPI import StripeAPI


class StripeAPIAdapter(PaymentAPIAdapter):
    """Stripe API Adapter class"""

    def __init__(self, stripe_key):
        self.stripe_api = StripeAPI(stripe_key)

    def pay(self, amount):
        self.stripe_api.stripe_payment(amount)

    def refund(self, amount):
        self.stripe_api.stripe_refund(amount)
