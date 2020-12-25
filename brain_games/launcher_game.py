"""Main module of brain-games."""

from brain_games import cli


def launch_game(game):
    """launch games.

    Args:
        name_game: str

    Returns:
        Return query to player.
    """
    print('Welcome to the Brain Games!')  # noqa: WPS421
    name = cli.welcome_user('May I have your name? ')
    print('Hello, {a}!'.format(a=name))  # noqa: WPS421
    print(game.get_data_of_game()[0])  # noqa: WPS421
    index = 0
    while index < 3:
        (question, true_answer) = (game.get_data_of_game()[1])  # noqa: WPS421
        answer = cli.welcome_user((
            'Question: {a}\n'
            +
            'Your answer: '
            ).format(a=question),
        )
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
