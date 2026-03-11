

article = str(input("Enter the article name: "))

def price_required():
    try:
        price = float(input("Enter the price of the item: "))

        if price <= 0:
            print("try again")
            return price_required()
    except ValueError:
        print("try again")
        return price_required()
    return price


def required_quantity():
    try:
        amount = int(input("Enter the amount: "))
        if amount <= 0:
            print("try again")
            return required_quantity()
    except ValueError:
        print("try again")
        return required_quantity()
    return amount

price = price_required()
amount = required_quantity()

total_cost = (price * amount)


print(f"Product name: {article}")
print(f"Product price: {price}")
print(f"Product quantity: {amount}")
print(f"Total calculated cost: {total_cost}")