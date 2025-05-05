from products import Product
from store import Store


def total_amount(store):
    pass


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
        3: "",
        4: exit,
    }

    while True:
        print("""
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

    user_choice_main_menu = start(best_buy)

    """try:
        print(bose.buy(50))
        print(mac.buy(100))
    except ValueError:
        print('Error while making order! Quantity larger than what exists')"""



if __name__ == "__main__":
    main()