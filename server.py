import stripe

stripe.api_key = "sk_test_your_key_here"

def create_payment(amount, currency):
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
    )
    return intent

def create_customer(email):
    customer = stripe.Customer.create(
        email=email,
    )
    return customer
