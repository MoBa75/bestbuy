class Product:

    def __init__(self, name, price, quantity):
        if not isinstance(name, str):
            raise TypeError(f"Expected 'name' to be str, got {type(name).__name__}!")
        if not isinstance(price, float):
            raise TypeError(f"Expected 'price' to be float, got {type(price).__name__}!")
        if price <= 0:
            raise ValueError("Price hase to be a positiv number!")
        if not isinstance(quantity, int):
            raise TypeError(f"Expected 'quantity' to be int, got {type(quantity).__name__}")
        if quantity < 0:
            raise ValueError("Quantity can not be negative!")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def get_quantity(self):  # -> int
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("ERROR: Product can't have a negativ quantity")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):  # -> bool
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def __str__(self):
        if self.active:
            return f"{self.name} - Price: ${self.price}, Quantity: {self.quantity}"
        else:
            return ""

    def buy(self, quantity):  # -> float
        order_quantity = self.quantity - quantity
        if order_quantity < 0:
            raise ValueError('Quantity larger than what exists')
        self.set_quantity(order_quantity)
        return float(quantity * self.price)
