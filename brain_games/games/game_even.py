"""Main module of game brain-even."""

import random

DESCRIPTION = ('Answer "yes" if the number is even,'
               ' otherwise answer "no".')


def is_even(num):
    """Check num even or uneven.

    Args:
        num: int

    Returns:
        Return True or False.
    """
    return num != 0 and num % 2 == 0


def generate_round():
    """Ask question and push true answer.

    Returns:
        Return question to player,
        true answer.
    """
    num = random.randint(0, 100)  # noqa: S311
    if is_even(num) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return num, answer
