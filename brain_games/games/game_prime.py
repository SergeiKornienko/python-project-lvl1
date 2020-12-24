"""Main module of game brain-prime."""

import random


def game_prime():
    """Ask question and push true answer.

    Returns:
        Return rules of the game,
        question to player,
        true answer.
    """
    arg = random.randint(1, 100)  # noqa: S311, WPS432
    question = str(arg)
    intro = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    index = 2
    while index <= arg / 2:
        if arg % index == 0:
            return (intro, (question, 'no'))
        index += 1
    return (intro, (question, 'yes'))
