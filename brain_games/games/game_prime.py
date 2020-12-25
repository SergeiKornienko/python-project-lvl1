"""Main module of game brain-prime."""

import random


def get_data_of_game():
    """Ask question and push true answer.

    Returns:
        Return rules of the game,
        question to player,
        true answer.
    """
    begin_interval_nums = 1
    end_interval_nums = 100
    arg = random.randint(begin_interval_nums, end_interval_nums)  # noqa: S311
    question = str(arg)
    intro = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    index = 2
    while index <= arg / 2:
        if arg % index == 0:
            return (intro, (question, 'no'))
        index += 1
    return (intro, (question, 'yes'))
