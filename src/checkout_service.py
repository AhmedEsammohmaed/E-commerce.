from typing import Dict
from .models.product import Product
from .models.shipping import Shipping
from .models.customer import Customer

class CheckoutService:
    SHIPPING_FEES_PER_KG = 30  # EGP per kg

    def checkout(self, customer: Customer, cart):
        if cart.is_empty():
            raise ValueError("Cart is empty")

        subtotal = 0
        shipping_items: Dict[str, Dict[str, float]] = {}
        total_weight_grams = 0

        for product, qty in cart.get_items().items():
            if product.is_expired():
                raise ValueError(f"{product.name} is expired")
            if product.quantity < qty:
                raise ValueError(f"{product.name} is out of stock")

            subtotal += product.price * qty

            if isinstance(product, Shipping):
                total_weight_grams += qty * product.get_weight()
                shipping_items[product.name] = {
                    "qty": qty,
                    "unit_weight": product.get_weight(),
                    "price": product.price,
                }

        shipping_cost = (total_weight_grams / 1000) * self.SHIPPING_FEES_PER_KG
        total_amount = subtotal + shipping_cost

        if customer.get_balance() < total_amount:
            raise ValueError("Insufficient balance")

        customer.deduct_amount(total_amount)

        # Reduce stock
        for product, qty in cart.get_items().items():
            product.reduce_quantity(qty)

        # Shipment notice
        if shipping_items:
            print("** Shipment notice **")
            for name, info in shipping_items.items():
                qty = info["qty"]
                weight = info["unit_weight"] * qty
                print(f"{qty}x {name} {weight:.0f}g {qty * info['price']:.0f} EGP")
            print(f"Total package weight {total_weight_grams/1000:.1f}kg\n")

        # Checkout receipt
        print("** Checkout receipt **")
        for product, qty in cart.get_items().items():
            print(f"{qty}x {product.name} {qty * product.price:.0f} EGP")
        print("----------------------")
        print(f"Subtotal {subtotal:.0f} EGP")
        print(f"Shipping {shipping_cost:.0f} EGP")
        print(f"Amount {total_amount:.0f} EGP")
        print(f"Customer balance after payment: {customer.get_balance():.0f} EGP")
