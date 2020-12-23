"""Main module of game brain-calc."""

import random


def game_calc():
    """Ask question and check of calculations.

    Returns:
        Return rules of the game,
        question to player,
        true answer.
    """
    intro = 'What is the result of the expression?'
    arg1 = random.randint(0, 20)  # noqa: S311, WPS432
    arg2 = random.randint(0, 20)  # noqa: S311, WPS432
    operation = random.randint(1, 3)  # noqa: S311, WPS432
    if operation == 1:
        task = ('{a} + {b}'.format(a=arg1, b=arg2), str(arg1 + arg2))
    elif operation == 2:
        task = ('{a} - {b}'.format(a=arg1, b=arg2), str(arg1 - arg2))
    elif operation == 3:
        task = ('{a} * {b}'.format(a=arg1, b=arg2), str(arg1 * arg2))
    return (intro, task)
