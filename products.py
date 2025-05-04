
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.activ = True #auf Menge achten - ab mindestens 1


    def get_quantity(self):         #-> int
        return self.quantity


    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError ("ERROR: Product can't have a negativ quantity")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self):            #-> bool
        return self.activ


    def activate(self):
        self.activ = True


    def deactivate(self):
        self.activ = False


    def __str__(self):              #-> str
        return f"{self.name} - Price: ${self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):        #-> float
        order_quantity = self.quantity - quantity
        if order_quantity < 0:
            raise ValueError ('Error while making order! Quantity larger than what exists')
        self.set_quantity(order_quantity)
        return float(quantity * self.price)

