#!/usr/bin/env python
"""Script for launch brain-prime."""

from brain_games import engine
from brain_games.games import game_prime


def main():
    """Launch game_prime()."""
    engine.run(game_prime)


if __name__ == '__main__':
    main()
