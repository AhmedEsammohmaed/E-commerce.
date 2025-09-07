from datetime import date
from typing import Optional

class Product:
    def __init__(self, name: str, price: float, quantity: int, expiry_date: Optional[date] = None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.expiry_date = expiry_date

    def is_expired(self) -> bool:
        return self.expiry_date is not None and self.expiry_date < date.today()

    def reduce_quantity(self, amount: int):
        if amount > self.quantity:
            raise ValueError("Not enough stock available")
        self.quantity -= amount
