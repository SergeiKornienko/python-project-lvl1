#!/usr/bin/env python
"""Script for launch brain-prime."""

from brain_games import launcher_game
from brain_games.games import game_prime


def main():
    """Launch game_prime()."""
    launcher_game.launch_game(game_prime)


if __name__ == '__main__':
    main()
