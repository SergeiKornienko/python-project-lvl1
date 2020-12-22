"""Main module of game brain-even."""

import random

from brain_games import check_even, cli


def game_even():
    """Power game brain-even.

    Returns:
        Return query to player.
    """
    print('Welcome to the Brain Games!')  # noqa: WPS421
    name = cli.welcome_user('May I have your name? ')
    print('Hello, {a}!'.format(a=name))  # noqa: WPS421
    print(  # noqa: WPS421
        'Answer "yes" if the number is even, otherwise answer "no".',
          )
    index = 0
    while index < 3:
        num = random.randint(0, 100)  # noqa: S311
        answer = cli.welcome_user('Question: {a}\nYour answer: '.format(a=num))
        num_even = check_even.check_even(num)
        if answer == num_even:
            print('Correct!')  # noqa: WPS421
        elif answer == num_even:
            print('Correct!')  # noqa: WPS421
        else:
            print(  # noqa: WPS421
                ("'{a}' is wrong answer ;). Correct answer was '{b}'."
                 ).format(a=answer, b=num_even),
                )
            return print(  # noqa: WPS421
                "Let's try again, {a}!".format(a=name),
            )
        index += 1
    return print(  # noqa: WPS421
        'Congratulations, {a}!'.format(a=name),
        )
