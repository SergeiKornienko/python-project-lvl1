"""Main module of game brain-even."""

from brain_games import cli
from brain_games import choice_game
from brain_games import greeting

from brain_games.games import game_even

def game_summon(name_game):
    """Power game brain-even.

    Returns:
        Return query to player.
    """
    name = greeting.greet()
    
    index = 0
    while index < 3:
        if name_game == 'even':
            (intro, question, true_answer) = game_even.game_even()
        if index == 0:
            print(intro)  # noqa: WPS421
        answer = cli.welcome_user('Question: {a}\nYour answer: '.format(a=question))  # noqa: WPS421
        if answer == true_answer:
            print('Correct!')  # noqa: WPS421
        else:
            print(  # noqa: WPS421
                ("'{a}' is wrong answer ;). Correct answer was '{b}'."
                ).format(a=answer, b=true_answer),
                )
            return print(  # noqa: WPS421
            "Let's try again, {a}!".format(a=name),
            )
        index += 1
    return print(  # noqa: WPS421
        'Congratulations, {a}!'.format(a=name),
        )
