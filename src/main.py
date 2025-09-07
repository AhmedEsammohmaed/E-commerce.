from datetime import date, timedelta
from models.product import Product
from models.shipping import Shipping
from models.customer import Customer
from cart import Cart
from checkout_service import CheckoutService

def main():
    # Products
    cheese = Shipping("Cheese", 100, 5, 200, date.today() + timedelta(days=2))
    tv = Shipping("TV", 1000, 3, 5000)
    scratch_card = Product("Mobile Scratch Card", 50, 10)

    # Customer
    customer = Customer(4000)

    # Cart
    cart = Cart()
    try:
        cart.add(cheese, 2)
        cart.add(tv, 3)
        cart.add(scratch_card, 1)

        checkout = CheckoutService()
        checkout.checkout(customer, cart)

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
