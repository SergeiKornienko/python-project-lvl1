"""Main module of game brain-gcd."""

import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def calc_gcd(num1, num2):
    """Find the greatest common divisor of given numbers.

    Args:
        num1: int
        num2: int

    Returns:
        Return greatest common divisor.
    """
    divider = min(num1, num2)  # noqa: S311
    while divider >= 1:
        if num1 % divider == 0 and num2 % divider == 0:
            return divider
        divider -= 1


def generate_round():
    """Ask question and push true answer.

    Returns:
        Return question to player,
        true answer.
    """
    num1 = random.randint(1, 20)  # noqa: S311
    num2 = random.randint(1, 20)  # noqa: S311
    return ('{a} {b}'.format(a=num1, b=num2),
            str(calc_gcd(num1, num2)))
