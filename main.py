from products import Product
from store import Store


def make_order(store):
    order_list = []
    inventory = store.get_all_products()
    list_all_products(store)
    print("______\nWhen you want to finish order, enter empty text.")
    while True:

        while True:
            user_choice_product = input('Which product # do you want? ')
            if not user_choice_product:
                break
            elif user_choice_product.isnumeric() and 0 < int(user_choice_product) <= len(inventory):
                user_choice_product = int(user_choice_product)
                break
            print('ERROR: Please choose the number from listed products or leave the input blank')

        while True:
            user_choice_amount = input('What amount do you want? ')
            if not user_choice_amount:
                break
            elif user_choice_amount.isnumeric():
                user_choice_amount = int(user_choice_amount)
                break
            print('ERROR: Please enter a whole number or leave the input blank')

        if not user_choice_product or not user_choice_amount:
            break
        order_list.append((inventory[user_choice_product - 1], user_choice_amount))
        print('Product added to list!')

    if order_list:
        print(store.order(order_list))


def total_amount(store):
    inventory_quantity = store.get_total_quantity()
    print(f'Total of {inventory_quantity} items in store')


def list_all_products(store):
    inventory = store.get_all_products()
    for index, product in enumerate(inventory):
        print(f'{index + 1}. {product}')


def user_input_main_menu():
    while True:
        user_input = input('Please choose a number: ')
        if user_input.isnumeric() and 0 < int(user_input) < 5:
            return int(user_input)
        else:
            print('Enter a numer between 1 and 4!')


def start(store):
    func_dict = {
        1: list_all_products,
        2: total_amount,
        3: make_order,
        4: exit,
    }
    while True:
        print("""
   Store Menu
   __________
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""")
        user_input = user_input_main_menu()
        if user_input == 4:
            func_dict[user_input]()
        func_dict[user_input](store)


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
