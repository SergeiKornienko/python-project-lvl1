from brain_games import cli

def greet():
    print('Welcome to the Brain Games!')  # noqa: WPS421
    name = cli.welcome_user('May I have your name? ')
    print('Hello, {a}!'.format(a=name))  # noqa: WPS421
    return name