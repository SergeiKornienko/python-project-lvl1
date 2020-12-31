#!/usr/bin/env python
"""Script for launch brain-gcd."""

from brain_games import engine
from brain_games.games import game_gcd


def main():
    """Launch game_gcd()."""
    engine.run(game_gcd)


if __name__ == '__main__':
    main()
