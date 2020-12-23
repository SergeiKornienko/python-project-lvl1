"""Main module of game brain-even."""

import random


def game_even():
    """Ask question and check num even or uneven.

    Returns:
        Return rules of the game,
        answer of player,
        true answer.
    """
    intro = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = random.randint(0, 100)  # noqa: S311
    if question == 0 or question % 2 != 0:
        true_answer = 'no'
    else:
        true_answer = 'yes'
    return (intro, (question, true_answer))
