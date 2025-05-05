
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
       return self.products


    def order(self, shopping_list):
        price = 0.0
        for product in shopping_list:
            price += product[0].price * product[1]
        return price







