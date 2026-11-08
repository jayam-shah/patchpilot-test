import stripe

stripe.api_key = "sk_test_your_key_here"

def create_payment(amount, currency):
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        # Add the `stripe_version` parameter to the request
        stripe_version='2026-10-28.endive',
    )
    return intent

def create_customer(email):
    customer = stripe.Customer.create(
        email=email,
        # Add the `stripe_version` parameter to the request
        stripe_version='2026-10-28.endive',
    )
    return customer

---END CODE---