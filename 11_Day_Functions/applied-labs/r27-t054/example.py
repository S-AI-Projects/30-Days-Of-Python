def validate_quantity(quantity):
    """Reject negative quantities."""
    if quantity < 0:
        raise ValueError("quantity must not be negative")


def price(quantity, *, unit_price, discount=0):
    validate_quantity(quantity)
    return quantity * unit_price * (1 - discount)


if __name__ == "__main__":
    print(price(3, unit_price=10, discount=0.1))
    print(price(0, unit_price=10, discount=0.1))