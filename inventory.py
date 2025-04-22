class Product:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        if amount > 0:
            self.quantity += amount
        else:
            raise ValueError("Amount to add should be positive")

    def remove_stock(self, amount):
        if 0 < amount <= self.quantity:
            self.quantity -= amount
        else:
            raise ValueError("Insufficient stock or invalid amount")

    def get_stock_value(self):
        return self.price * self.quantity


class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def is_expired(self, current_date):
        return current_date > self.expiration_date
