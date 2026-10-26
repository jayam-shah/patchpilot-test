import stripe

stripe.api_key = "sk_test_your_key_here"

def create_payment(amount, currency):
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        stripe_version='2026-09-30.endive'
    )
    return intent

def create_customer(email):
    customer = stripe.Customer.create(
        email=email,
        stripe_version='2026-09-30.endive'
    )
    return customer

---END CODE---