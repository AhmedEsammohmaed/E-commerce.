class Customer:
    def __init__(self, balance: float):
        self.balance = balance

    def get_balance(self) -> float:
        return self.balance

    def deduct_amount(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
