#!/usr/bin/env python

from brain_games import cli


def intro(greet):
    print(greet)


def main():
    intro('Welcome to the Brain Games!')
    cli.welcome_user()


if __name__ == '__main__':
    main()
