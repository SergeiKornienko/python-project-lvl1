"""Main module of game brain-gcd."""

import random


def game_gcd():
    """Ask question and push true answer.

    Returns:
        Return rules of the game,
        question to player,
        true answer.
    """
    intro = 'Find the greatest common divisor of given numbers.'
    arg1 = random.randint(1, 20)  # noqa: S311, WPS432
    arg2 = random.randint(1, 20)  # noqa: S311, WPS432
    question = '{a} {b}'.format(a=arg1, b=arg2)
    divider = min(arg1, arg2)  # noqa: S311, WPS432
    while divider >= 1:
        if arg1 % divider == 0 and arg2 % divider == 0:
            return (intro, (question, str(divider)))
        divider -= 1
