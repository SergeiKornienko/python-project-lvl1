#!/usr/bin/env python
"""Script for launch brain-even."""

from brain_games import launcher_game
from brain_games.games import game_even


def main():
    """Launch game_even()."""
    launcher_game.launch_game(game_even)


if __name__ == '__main__':
    main()
