import prompt, random


def game_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    while index < 3:
        num = random.randint(0, 100)
        answer = prompt.string('Question: {}\nYour answer: '.format(num))
        if num % 2 == 0:
            num_even = True
        else:
            num_even = False
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
