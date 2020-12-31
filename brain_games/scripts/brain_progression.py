#!/usr/bin/env python
"""Script for launch brain-progression."""

from brain_games import engine
from brain_games.games import game_progression


def main():
    """Launch game_progression()."""
    engine.run(game_progression)


if __name__ == '__main__':
    main()
