#!/usr/bin/env python
"""Scripts for launch brain-calc."""

from brain_games import engine
from brain_games.games import game_calc


def main():
    """Launch game_calc()."""
    engine.run(game_calc)


if __name__ == '__main__':
    main()
