from .product import Product

class Shipping(Product):
    def __init__(self, name: str, price: float, quantity: int, weight: float, expiry_date=None):
        super().__init__(name, price, quantity, expiry_date)
        self.weight = weight  # grams

    def get_weight(self) -> float:
        return self.weight
