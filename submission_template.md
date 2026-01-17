# AI Code Review Assignment (Python)

## Candidate
- Name: Bereket Lingerew
- Approximate time spent: 70 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The function divides by the total number of orders, even though it excludes cancelled orders from the numerator. This produces an incorrect average whenever cancelled orders are present.
- If the input is empty, it raises a ZeroDivisionError.

### Edge cases & risks
- If all orders are cancelled, the intended average is undefined. The current code returns 0 divided by total order count, which is misleading.
- Missing keys like `status` or `amount` raise KeyError.
- Non numeric `amount` values can raise TypeError.

### Code quality / design issues
- Assumes `orders` is a list of well formed dicts with required keys.
- No documentation about expected behavior when there are no valid orders.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Track `valid_count` for non cancelled orders and divide by that value.
- Return `0.0` when there are no qualifying orders.
- Make the function resilient to missing keys and non numeric amounts by skipping malformed entries.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Mixed statuses: some cancelled, some active, to confirm cancelled orders do not affect the denominator.
- All cancelled orders, to confirm the empty qualifying set behavior.
- Empty input, to confirm it does not crash.
- Malformed orders (missing fields, invalid amounts), to confirm they do not crash and are skipped.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The original code divides by the total number of orders, not the number of non cancelled orders, so cancelled orders still affect the result.
- The explanation claims correct exclusion, but the denominator logic contradicts that.
- It does not mention the division by zero risk for empty input.

### Rewritten explanation
- This function computes the average amount of non cancelled orders by summing the amounts of all orders whose status is not `cancelled`, then dividing by the count of those qualifying orders. If there are no qualifying orders, it returns `0.0`.

## 4) Final Judgment
- Decision: Request Changes
- Justification: Incorrect denominator and missing edge case handling can produce wrong business metrics or runtime errors.
- Confidence & unknowns: High confidence. The only unknown is the desired behavior when there are zero qualifying orders (returned as 0.0 in the fix).

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The function treats any string containing `@` as valid, so many invalid emails are counted as valid.

### Edge cases & risks
- Values that are not strings can cause unexpected behavior if they contain `@` through custom `__contains__` logic, or can raise errors depending on type.
- Obvious invalid cases like `"@"`, `"a@"`, or `"a@b"` are counted as valid.

### Code quality / design issues
- The function name implies email validation, but the validation rule is far too weak.
- No documentation of what “valid” means.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Require input item to be a string.
- Apply lightweight validation:
  - exactly one `@`
  - non empty local and domain parts
  - no spaces
  - domain contains a dot and does not start or end with a dot
  - reject consecutive dots in the domain

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- A mix of valid and invalid emails to confirm only valid ones are counted.
- Boundary cases: missing local part, missing domain part, multiple `@` symbols.
- Domain formatting: no dot, starts with dot, ends with dot, consecutive dots.
- Non string values (None, ints) to confirm they are ignored safely.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- The original implementation does not actually validate emails beyond checking `@`.
- It does not explicitly ignore invalid entries, it incorrectly counts many invalid entries.

### Rewritten explanation
- This function counts how many items in the input are email like strings. It uses a lightweight validation rule (one `@`, non empty local and domain, no spaces, and a dotted domain) and ignores non string or malformed values.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The implementation does not match the implied intent of “valid email” counting.
- Confidence & unknowns: High confidence. Exact email validation strictness can vary, so the final rule set may need tuning depending on product requirements.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The function divides by `len(values)` even though it excludes `None` values from the numerator, producing an incorrect average.
- Empty input raises ZeroDivisionError.

### Edge cases & risks
- Strings that cannot be converted to float raise ValueError.
- Values like `float('nan')` or `float('inf')` can silently poison results if not handled.
- If all values are None, the original returns 0 divided by total length, which is misleading.

### Code quality / design issues
- Assumes all non None values are numeric or float convertible.
- No clear definition of what should happen when there are no valid values.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only values that successfully convert to finite floats.
- Divide by the count of valid numeric values.
- Return `0.0` when there are no valid measurements.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

- Typical numeric list input to confirm correct averaging.
- Mixed list including None to ensure None is excluded from denominator.
- Mixed types: numeric strings and non numeric strings to ensure safe skipping.
- Empty input and all invalid input to confirm safe `0.0` result.
- NaN and Infinity values to confirm they are ignored.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- The original code does not average the remaining values correctly because it divides by total length.
- It does not safely handle mixed input types because `float(v)` can raise.
- It does not mention the empty input crash.

### Rewritten explanation
- This function calculates the average of valid measurements by ignoring `None` and any values that cannot be converted to a finite float. It sums the valid numeric measurements and divides by the number of valid values. If no valid measurements exist, it returns `0.0`.

## 4) Final Judgment
- Decision: Request Changes
- Justification: Incorrect denominator causes wrong averages and unhandled conversion errors can crash at runtime.
- Confidence & unknowns: High confidence. The only potential requirement ambiguity is what the return value should be when no valid measurements exist.
