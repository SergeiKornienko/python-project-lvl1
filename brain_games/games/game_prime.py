"""Main module of game brain-prime."""

import random

DESCRIPTION = ('Answer "yes" if given number is prime.'
               ' Otherwise answer "no".')


def is_prime(num):
    """Check num even or uneven.

    Args:
        num: int

    Returns:
        Return bool.
    """
    if num == 1:
        return False
    index = 2
    while index <= num / 2:
        if num % index == 0:
            return False
        index += 1
    return True


def generate_round():
    """Ask question and push true answer.

    Returns:
        Return question to player,
        true answer.
    """
    num = random.randint(1, 100)  # noqa: S311
    if is_prime(num) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return num, answer
