"""Main module of game brain-progression."""

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
    arg1 = random.randint(begin_interval_nums, end_interval_nums)  # noqa: S311
    begin_interval_prorgess = 1
    end_interval_prorgess = 10
    arg2 = random.randint(  # noqa: S311
        begin_interval_prorgess, end_interval_prorgess)
    begin_miss_num = 0
    end_miss_num = 9
    miss_number = random.randint(begin_miss_num, end_miss_num)  # noqa: S311
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
        (question, str(arg1 + arg2 * miss_number)))
