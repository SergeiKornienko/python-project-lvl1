"""Main module of game brain-progression."""

import random


def game_progression():
    """Ask question and push true answer.

    Returns:
        Return rules of the game,
        question to player,
        true answer.
    """
    arg1 = random.randint(1, 100)  # noqa: S311, WPS432
    arg2 = random.randint(1, 10)  # noqa: S311, WPS432
    miss_number = random.randint(0, 9)  # noqa: S311, WPS432
    question = ''
    index = 0
    while index <= 9:
        if index == miss_number:
            question = '{a}.. '.format(a=question)
        else:
            question += '{a} '.format(a=str(arg1 + arg2 * index))
        index += 1
    return (
        'What number is missing in the progression?',
        (question, str(arg1 + arg2 * miss_number)),
         )
