#!/usr/bin/env python
"""Script for launch brain-even."""

from brain_games import engine
from brain_games.games import game_even


def main():
    """Launch game_even()."""
    engine.run(game_even)


if __name__ == '__main__':
    main()
