"""Main module of game brain-even."""

import random

DESCRIPTION = ('Answer "yes" if the number is even,'
               ' otherwise answer "no".')


def check_even(num):
    """Check num even or uneven.

    Args:
        num: int

    Returns:
        Return string 'yes' or 'no'.
    """
    return 'no' if num == 0 or num % 2 != 0 else 'yes'


def generate_round():
    """Ask question and push true answer.

    Returns:
        Return question to player,
        true answer.
    """
    num = random.randint(0, 100)  # noqa: S311
    return (num, check_even(num))
