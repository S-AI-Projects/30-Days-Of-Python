def apply_changes(stock, changes):
    """Apply signed stock changes. Raise ValueError if any stock goes negative.
    The original dictionary is never modified."""
    new_stock = dict(stock)  # work on a copy
    for item, change in changes.items():
        new_stock[item] = new_stock.get(item, 0) + change
        if new_stock[item] < 0:  # decisive condition
            raise ValueError(f"Stock for '{item}' would be negative")
    return new_stock


if __name__ == "__main__":
    print(apply_changes({"tea": 3}, {"tea": -2, "coffee": 4}))