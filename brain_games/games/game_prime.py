"""Main module of game brain-prime."""

import random

DESCRIPTION = ('Answer "yes" if given number is prime.'
               ' Otherwise answer "no".')


def chek_prime(num):
    """Check num even or uneven.

    Args:
        num: int

    Returns:
        Return string 'yes' or 'no'.
    """
    index = 2
    while index <= num / 2:
        if num % index == 0:
            return 'no'
        index += 1
    return 'yes'


def generate_round():
    """Ask question and push true answer.

    Returns:
        Return question to player,
        true answer.
    """
    num = random.randint(1, 100)  # noqa: S311
    return (num, chek_prime(num))
