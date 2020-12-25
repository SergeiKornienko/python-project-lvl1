#!/usr/bin/env python
"""Scripts for launch brain-calc."""

from brain_games import launcher_game
from brain_games.games import game_calc


def main():
    """launch game_calc()."""
    launcher_game.launch_game(game_calc)


if __name__ == '__main__':
    main()
