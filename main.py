from products import Product
from store import Store


def make_order(store):
    """
    Lets the user create an order by selecting products and quantities.
    Displays all available products and prompts the user to choose a
    product number and amount. The order can be finalized by submitting
    an empty input.
    :param store: Class Store instance
    """
    order_list = []
    inventory = store.get_all_products()
    list_all_products(store)
    print("------\nWhen you want to finish order, enter empty text.")
    while True:

        while True:
            user_choice_product = input('Which product # do you want? ')
            if not user_choice_product:
                break
            elif (user_choice_product.isnumeric()
                  and 0 < int(user_choice_product) <= len(inventory)):
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
    """
    Displays the total quantity of all products available in the store.
    :param store: Class Store instance
    """
    inventory_quantity = store.get_total_quantity()
    print(f'Total of {inventory_quantity} items in store')


def list_all_products(store):
    """
    Displays a list of all products available in the store.
    :param store: Class Store instance
    """
    inventory = store.get_all_products()
    for index, product in enumerate(inventory):
        print(f'{index + 1}. {product}')


def user_input_main_menu():
    """
    Prompts the user to select an option from the main menu by entering a number.
    The user is repeatedly asked to input a number until a valid choice (1-4) is
    entered. Only numeric inputs within the valid range are accepted.
    :return:user input between 1 and 4 as integer
    """
    while True:
        user_input = input('Please choose a number: ')
        if user_input.isnumeric() and 0 < int(user_input) < 5:
            return int(user_input)
        else:
            print('Enter a numer between 1 and 4!')


def start(store):
    """
    Launches the main store menu and calls functions by user selection.
    Ends the programm if no more products available in the store.
    :param store: Class Store instance
    """
    func_dict = {
        1: list_all_products,
        2: total_amount,
        3: make_order,
        4: exit,
    }
    while True:
        print("""
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""")
        if store.get_total_quantity() == 0:
            print('No more products available. Goodbye!')
            break
        user_input = user_input_main_menu()
        if user_input == 4:
            func_dict[user_input]()
        func_dict[user_input](store)


def main():
    """Creates Store instance with Product instances and starts the programm."""
    product_list = [Product("MacBook Air M2", price=1450.0, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250.0, quantity=500),
                    Product("Google Pixel 7", price=500.0, quantity=250)
                    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
