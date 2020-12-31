#!/usr/bin/env python
"""Scripts for power brain-games."""

from brain_games import cli


def intro(greet):
    """Take sring and print.

    Args:
        greet: str

    """
    print(greet)  # noqa:WPS421


def main():
    """Print greeting."""
    intro('Welcome to the Brain Games!')
    name = cli.welcome_user('May I have your name? ')
    print('Hello, {a}!'.format(a=name))  # noqa:WPS421


if __name__ == '__main__':
    main()
