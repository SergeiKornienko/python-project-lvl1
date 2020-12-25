#!/usr/bin/env python
"""Script for launch brain-gcd."""

from brain_games import launcher_game
from brain_games.games import game_gcd


def main():
    """Launch game_gcd()."""
    launcher_game.launch_game(game_gcd)


if __name__ == '__main__':
    main()
