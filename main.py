from products import Product
from store import Store


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    best_buy = Store([bose, mac])

    pixel = Product("Google Pixel 7", price=500, quantity=250)
    best_buy.add_product(pixel)

    try:
        print(bose.buy(50))
        print(mac.buy(100))
    except ValueError:
        print('Error while making order! Quantity larger than what exists')

    """print(mac.is_active())

    print(bose)
    print(mac)

    bose.set_quantity(1000)
    print(bose)

    print(bose.get_quantity())
    print(best_buy.get_all_products())

    best_buy = Store([bose, mac])
    price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
    print(f"Order cost: {price} dollars.")"""

    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))

if __name__ == "__main__":
    main()