#!/usr/bin/env python

from brain_games import cli


def intro(greet):
    print(greet)


def main():
    intro('Welcome to the Brain Games!')
    name = cli.welcome_user('May I have your name? ')
    print('Hello, {}!'.format(name))


if __name__ == '__main__':
    main()
