from products import Product


class Store:
    """
    Represents a store that manages a collection of products.

    Attributes:
        Products (list): list of Product objects
    """

    def __init__(self, products):
        """
        Initializes a Store instance with a list of Product instances.
        :param products: List of Product instances
        """
        if not isinstance(products, list):
            raise TypeError(f"Expected products to be a list, got {type(products).__name__}!")
        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Expected list entries to be a "
                                f"Product, got {type(product).__name__}!")
        self.products = products

    def add_product(self, product):
        """
        Adds a Product instance to the store's inventory.
        :param product: Class Product instance
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a Product instance from the store's inventory.
        :param product: Class Product instance
        """
        self.products.remove(product)

    def get_total_quantity(self):
        """
        Calculates the total quantity of all Product instances in the store.
        :return: Total quantity as integer
        """
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        """
        Retrieves a list of all active (available) Product instances.
        :return: A list of active Product instances.
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """
        Processes a customer's shopping list and calculates the total price.
        If an order cannot be fulfilled, restores the original product quantities.
        :param shopping_list: List of tuple containing a Product instance and quantity as integer
        :return: A confirmation message with total price or an error message if
        the order fails as string
        """
        price = 0.0
        original_product_quantity = []
        for product in shopping_list:
            try:
                original_product_quantity.append(product[0].get_quantity())
                price += product[0].buy(product[1])
            except ValueError as error:
                product_reset = []
                for index, quantity in enumerate(original_product_quantity[:-1]):
                    if shopping_list[index][0] not in product_reset:
                        shopping_list[index][0].set_quantity(quantity)
                        product_reset.append(shopping_list[index][0])

                return f'\nError while making order! {error}'
        return f'********\nOrder made! Total payment: ${price}'
