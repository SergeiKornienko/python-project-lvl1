"""Main module of game brain-even."""
import prompt
import random
from brain_games import cli
from brain_games import check_even


def game_even():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    while index < 3:
        num = random.randint(0, 100)
        answer = cli.welcome_user('Question: {}\nYour answer: '.format(num))
        num_even = check_even.check_even(num)
        if answer == num_even:
            print('Correct!')
        elif answer == num_even:
            print('Correct!')
        else:
            print(
                ("'{}' is wrong answer ;). "+\
                "Correct answer was '{}'.").format(answer, num_even)
                )
            print("Let's try again, {}!".format(name))
            return
        index += 1
    return print('Congratulations, {}!'.format(name))
