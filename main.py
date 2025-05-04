import products as p


def main():
    bose = p.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = p.Product("MacBook Air M2", price=1450, quantity=100)

    try:
        print(bose.buy(50))
        print(mac.buy(101))
    except ValueError:
        print('Error while making order! Quantity larger than what exists')

    print(mac.is_active())

    print(bose)
    print(mac)

    bose.set_quantity(1000)
    print(bose)

if __name__ == "__main__":
    main()