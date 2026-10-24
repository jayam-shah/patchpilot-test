import stripe

stripe.api_key = "sk_test_your_key_here"

def create_payment(amount, currency):
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        # Add the `confirm` parameter to enable the `confirmCardPayment` method
        confirm=True,
    )
    return intent

def create_customer(email):
    customer = stripe.Customer.create(
        email=email,
        # Add the `description` parameter to provide a customer description
        description="Example customer",
    )
    return customer

---END CODE---

The updated code includes the `confirm` parameter in the `PaymentIntent.create` method to enable the `confirmCardPayment` method, and the `description` parameter in the `Customer.create` method to provide a customer description. These changes are necessary to ensure compatibility with the latest Stripe API version.