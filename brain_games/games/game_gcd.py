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
    begin_interval_nums = 1
    end_interval_nums = 20
    arg1 = random.randint(begin_interval_nums, end_interval_nums)  # noqa: S311
    arg2 = random.randint(begin_interval_nums, end_interval_nums)  # noqa: S311
    question = '{a} {b}'.format(a=arg1, b=arg2)
    divider = min(arg1, arg2)  # noqa: S311
    while divider >= 1:
        if arg1 % divider == 0 and arg2 % divider == 0:
            return (intro, (question, str(divider)))
        divider -= 1
