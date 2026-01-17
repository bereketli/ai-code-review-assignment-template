"""Task 3: Aggregate Valid Measurements.

Original behavior (buggy):
- Adds up all non-None values
- Divides by len(values), even if some values are None

Correct behavior:
- Average only over values that can be converted to finite floats
- Ignore None and non-numeric values safely
- Return 0.0 when no valid measurements exist
"""

from __future__ import annotations

import math
from typing import Iterable


def average_valid_measurements(values: Iterable[object]) -> float:
    """Compute the average of valid measurements.

    Valid measurements are those that:
    - are not None
    - can be converted to float
    - are finite (not NaN / Infinity)

    Args:
        values: Iterable containing measurements.

    Returns:
        Average of valid measurements, or 0.0 if none are valid.
    """

    total: float = 0.0
    valid_count: int = 0

    for v in values:
        if v is None:
            continue

        try:
            num = float(v)
        except (TypeError, ValueError):
            continue

        if not math.isfinite(num):
            continue

        total += num
        valid_count += 1

    if valid_count == 0:
        return 0.0

    return total / valid_count
