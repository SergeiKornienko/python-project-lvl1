"""Main module of game brain-even."""

import random


def game_even():
    """Ask question and check num even or uneven.

    Returns:
        Return rules of the game,
        question to player,
        true answer.
    """
    intro = 'Answer "yes" if the number is even, otherwise answer "no".'
    begin_interval_num = 0
    end_interval_num = 100
    question = random.randint(  # noqa: S311
        begin_interval_num, end_interval_num,
        )
    if question == 0 or question % 2 != 0:
        true_answer = 'no'
    else:
        true_answer = 'yes'
    return (intro, (question, true_answer))
