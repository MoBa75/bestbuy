class Store:

    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
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
