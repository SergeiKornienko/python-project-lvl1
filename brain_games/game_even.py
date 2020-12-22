import prompt, random
from brain_games import cli
from brain_games import check_even

def game_even():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    while index < 3:
        num = random.randint(0, 100)
        answer = prompt.string('Question: {}\nYour answer: '.format(num))
        num_even = check_even.check_even(num)
        if num_even == True:
            true = 'yes'
        else:
            true = 'no'
        if answer == 'yes' and num_even == True:
            print('Correct!')
        elif answer == 'no' and num_even == False:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;). Correct answer was '{}'".format(answer, true))
            print("Let's try again, {}!".format(name))
            return
        index += 1
    return print('Congratulations, {}!'.format(name))

game_even()