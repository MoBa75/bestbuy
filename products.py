class Product:
    """
    Represents a product with a name, price, quantity, and active status.

    Attributes:
        Name (string): The name of the product
        Price (float): Price of the product
        Quantity (integer): Quantity of the products
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a Product instance with a name, price, and quantity.
        :param name: Name of the product as string
        :param price: Price of the product as float
        :param quantity: Quantity of the product as integer
        """
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

    def get_quantity(self):
        """
        Returns the current quantity of the Product instance.
        :return: The number of available units as integer.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the Product instance and deactivates
        the Product instance if quantity is zero.
        :param quantity: Quantity as integer
        """
        if quantity < 0:
            raise ValueError("ERROR: Product can't have a negativ quantity")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """
        Checks if the Product instance is active.
        :return: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Activates the Product instance, making it available.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the Product instance, making it unavailable.
        """
        self.active = False

    def __str__(self):
        """
        Description of the Product instance if active.
        :return: Description as string
        """
        if self.active:
            return f"{self.name} - Price: ${self.price}, Quantity: {self.quantity}"
        else:
            return ""

    def buy(self, quantity):
        """
        Processes a purchase and updates the quantity of the Product instance.
        :param quantity: Quantity to subtract from Product instance quantity as integer
        :return: The total price for the purchase as float.
        """
        order_quantity = self.quantity - quantity
        if order_quantity < 0:
            raise ValueError('Quantity larger than what exists')
        self.set_quantity(order_quantity)
        return float(quantity * self.price)
