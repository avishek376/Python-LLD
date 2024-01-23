from StripeAPIAdapter import StripeAPIAdapter
from PayPalAPIAdapter import PayPalAPIAdapter

if __name__ == '__main__':
    stripe_api = StripeAPIAdapter('stripe_api_key')
    stripe_api.pay(100)
    stripe_api.refund(100)

    paypal_api = PayPalAPIAdapter('paypal_api_key')
    paypal_api.pay(1000)
    paypal_api.refund(100)
