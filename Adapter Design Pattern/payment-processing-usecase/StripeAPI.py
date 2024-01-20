class StripeAPI:
    """Stripe API working as a third party payment processor"""

    def __init__(self, api_key):
        self.api_key = api_key

    def stripe_payment(self, amount):
        print(f"Payment of {amount} made with Stripe")
        return True

    def stripe_refund(self, amount):
        print(f"Refund of {amount} made with Stripe")
        return True
