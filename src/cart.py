from typing import Dict
from .models.product import Product

class Cart:
    def __init__(self):
        self.items: Dict[Product, int] = {}

    def add(self, product: Product, quantity: int):
        if product.is_expired():
            raise ValueError(f"{product.name} is expired")
        if product.quantity < quantity:
            raise ValueError(f"Not enough stock for {product.name}")
        self.items[product] = self.items.get(product, 0) + quantity

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def get_items(self):
        return self.items
