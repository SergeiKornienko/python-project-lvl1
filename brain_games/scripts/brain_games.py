#!/usr/bin/env python
"""Scripts for power brain-games."""

from brain_games import cli


def main():
    """Print greeting."""
    print('Welcome to the Brain Games!')  # noqa:WPS421
    name = cli.welcome_user('May I have your name? ')
    print('Hello, {a}!'.format(a=name))  # noqa:WPS421


if __name__ == '__main__':
    main()
