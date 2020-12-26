"""Main module of game brain-calc."""

import random


def get_data_game():
    """Ask question and check of calculations.

    Returns:
        Return rules of the game,
        question to player,
        true answer.
    """
    intro_of_game = 'What is the result of the expression?'
    begin_interval_nums = 0
    end_interval_nums = 20
    arg1 = random.randint(begin_interval_nums, end_interval_nums)  # noqa: S311
    arg2 = random.randint(begin_interval_nums, end_interval_nums)  # noqa: S311
    choice_operation_begin = 1
    choice_operation_end = 3
    operation = random.randint(  # noqa: S311
        choice_operation_begin, choice_operation_end)
    if operation == 1:
        question_and_true_answer = (
            '{a} + {b}'.format(a=arg1, b=arg2), str(arg1 + arg2))
    elif operation == 2:
        question_and_true_answer = (
            '{a} - {b}'.format(a=arg1, b=arg2), str(arg1 - arg2))
    elif operation == 3:
        question_and_true_answer = (
            '{a} * {b}'.format(a=arg1, b=arg2), str(arg1 * arg2))
    return (intro_of_game, question_and_true_answer)
