"""Task 2: Count Valid Emails.

Original behavior (too permissive):
- Counts any value containing '@' as a valid email

Correct behavior:
- Count only emails that reasonably match common email rules:
  - must be a string
  - exactly one '@'
  - non-empty local and domain parts
  - no spaces
  - domain contains a dot (e.g. example.com)

Note: This is not a full RFC5322 validator (which is intentionally complex).
"""

from __future__ import annotations

from typing import Iterable


def _is_valid_email(email: str) -> bool:
    # Basic sanity checks
    if not email or " " in email:
        return False

    # Must contain exactly one '@'
    if email.count("@") != 1:
        return False

    local, domain = email.split("@")

    if not local or not domain:
        return False

    # Domain must contain at least one dot and not start or end with it
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False

    # Avoid consecutive dots in domain
    if ".." in domain:
        return False

    return True


def count_valid_emails(emails: Iterable[object]) -> int:
    """Count valid email-like strings.

    Args:
        emails: Iterable that may contain strings and other types.

    Returns:
        Number of items that pass a lightweight email validation.
    """

    count = 0

    for email in emails:
        if isinstance(email, str) and _is_valid_email(email.strip()):
            count += 1

    return count
