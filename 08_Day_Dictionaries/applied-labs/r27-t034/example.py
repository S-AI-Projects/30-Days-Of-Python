from typing import Dict

def apply_stock_changes(inventory: Dict[str, int], changes: Dict[str, int]) -> Dict[str, int]:
    """
    Apply signed stock changes to an inventory dictionary.
    Invariant: No item stock may become negative. 
    If any change violates this, raises ValueError and leaves the original unchanged.
    """
    for item, delta in changes.items():
        current = inventory.get(item, 0)
        if current + delta < 0:
            raise ValueError(f"Stock for '{item}' cannot become negative (current: {current}, delta: {delta}).")

    new_inventory = dict(inventory)
    for item, delta in changes.items():
        new_inventory[item] = new_inventory.get(item, 0) + delta

    return new_inventory
