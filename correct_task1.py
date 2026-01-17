"""Task 1: Average Order Value.

Original behavior (buggy):
- Sums amounts for orders that are not cancelled
- Divides by the total number of orders (including cancelled)

Correct behavior:
- Sums amounts for orders that are not cancelled
- Divides by the number of *non-cancelled* orders

Defensive choices:
- Returns 0.0 when there are no qualifying orders.
- Skips malformed entries (missing keys or non-numeric amounts).
"""

from __future__ import annotations

from typing import Any, Iterable, Mapping


def calculate_average_order_value(orders: Iterable[Mapping[str, Any]]) -> float:
    """Calculate the average order value excluding cancelled orders.

    Args:
        orders: An iterable of order dictionaries expected to include:
            - "status": order status string
            - "amount": numeric order amount

    Returns:
        Average amount across non-cancelled orders.
        Returns 0.0 if there are no non-cancelled orders.
    """

    total: float = 0.0
    valid_count: int = 0

    for order in orders:
        # Use .get() to avoid KeyError and treat missing status as non-cancelled
        status = order.get("status")
        if status == "cancelled":
            continue

        try:
            amount = float(order.get("amount", 0))
        except (TypeError, ValueError):
            # Skip orders with invalid numeric amounts
            continue

        total += amount
        valid_count += 1

    if valid_count == 0:
        return 0.0

    return total / valid_count
