from decimal import Decimal, ROUND_HALF_UP
from typing import Union

def reference_discount(price: float, discount_pct: float) -> float:
    """Simple reference implementation for behavioral comparison."""
    if not (0 <= discount_pct <= 100):
        raise ValueError("Percentage must be between 0 and 100")
    return round(price * (1.0 - discount_pct / 100.0), 2)

def apply_discount(price: Union[str, float, int, Decimal], discount_percent: Union[str, float, int, Decimal]) -> Decimal:
    """
    Calculate percentage discount using Decimal and round to two decimal places.
    Rejects percentages outside 0..100.
    """
    p = Decimal(str(price))
    d = Decimal(str(discount_percent))

    if d < 0 or d > 100:
        raise ValueError("Percentage must be between 0 and 100.")

    discount_amount = p * (d / Decimal('100'))
    final_price = p - discount_amount
    return final_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
