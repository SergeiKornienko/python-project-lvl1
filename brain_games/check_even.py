"""Check number even or uneven."""


def check_even(num):
    """Check num even or uneven.

    Args:
        num: int

    Returns:
        Return 'yes' or 'no'.
    """
    return 'no' if num == 0 or num % 2 != 0 else 'yes'
