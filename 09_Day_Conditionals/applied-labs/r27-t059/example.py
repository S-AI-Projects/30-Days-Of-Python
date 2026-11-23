"""R27-T059: Shipping bands conditional logic and state/invariant verification."""


def calculate_shipping(total):
    """Return shipping cost based on order total.

    - total >= 100: 0 (free shipping)
    - total >= 50: 5
    - 0 <= total < 50: 10
    - total < 0: raises ValueError
    """
    if not isinstance(total, (int, float)):
        raise TypeError("Order total must be numeric")
    if total < 0:
        raise ValueError(f"Negative order total rejected: {total}")

    if total >= 100:
        return 0
    elif total >= 50:
        return 5
    else:
        return 10


class ShoppingCart:
    """Stateful order accumulator verifying the state/invariant connecting input/state to output."""

    def __init__(self):
        self.items = []

    @property
    def total(self):
        return round(sum(self.items), 2)

    @property
    def shipping(self):
        return calculate_shipping(self.total)

    @property
    def grand_total(self):
        return round(self.total + self.shipping, 2)

    def add_item(self, price):
        """Add an item price to the cart; rejects negative prices."""
        if not isinstance(price, (int, float)):
            raise TypeError("Item price must be numeric")
        if price < 0:
            raise ValueError(f"Negative item price rejected: {price}")
        self.items.append(round(price, 2))

    def verify_invariant(self):
        """Verify the state invariant connecting cart state to shipping output.

        Invariant rules:
        1. total >= 0 always holds.
        2. total >= 100 => shipping == 0
        3. 50 <= total < 100 => shipping == 5
        4. 0 <= total < 50 => shipping == 10
        5. grand_total == total + shipping
        """
        t = self.total
        s = self.shipping
        if t < 0:
            return False, "Total cannot be negative"
        if t >= 100 and s != 0:
            return False, "Expected free shipping for total >= 100"
        if 50 <= t < 100 and s != 5:
            return False, "Expected 5 shipping for 50 <= total < 100"
        if 0 <= t < 50 and s != 10:
            return False, "Expected 10 shipping for total < 50"
        if self.grand_total != round(t + s, 2):
            return False, "Grand total must equal total + shipping"
        return True, "Invariant holds"


if __name__ == "__main__":
    for amt in (49.99, 50, 99.99, 100):
        print(f"Total ${amt} -> Shipping ${calculate_shipping(amt)}")

    try:
        calculate_shipping(-1)
    except ValueError as e:
        print("Negative total rejected:", e)

    cart = ShoppingCart()
    for price in (49.99, 0.01, 49.99, 0.01):
        cart.add_item(price)
        valid, msg = cart.verify_invariant()
        print(
            f"Added ${price:5.2f} | Total: ${cart.total:6.2f} | "
            f"Shipping: ${cart.shipping} | Grand Total: ${cart.grand_total:6.2f} | "
            f"Invariant: {msg}"
        )
