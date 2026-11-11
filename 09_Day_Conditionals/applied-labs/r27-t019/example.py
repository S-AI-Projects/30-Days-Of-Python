"""Shipping-cost conditionals and a small input-scale demonstration."""


def shipping_cost(total: float) -> int:
    """Return shipping cost for an order total, rejecting negative totals."""
    if total < 0:
        raise ValueError("order total cannot be negative")
    if total >= 100:
        return 0
    elif total >= 50:
        return 5
    return 10


def calculate_shipping_costs(totals: list[float]) -> tuple[list[int], int]:
    """Return costs and the number of totals evaluated."""
    costs = []
    operation_count = 0
    for total in totals:
        costs.append(shipping_cost(total))
        operation_count += 1
    return costs, operation_count


if __name__ == "__main__":
    inputs = [49.99, 50, 99.99, 100]
    costs, operation_count = calculate_shipping_costs(inputs)
    print(f"inputs={inputs} costs={costs} operation_count={operation_count}")

    for size in (4, 40, 400):
        scale_inputs = inputs * (size // len(inputs))
        scale_costs, scale_operations = calculate_shipping_costs(scale_inputs)
        print(
            f"input_count={size} operation_count={scale_operations} "
            f"correct={scale_costs == costs * (size // len(costs))}"
        )
