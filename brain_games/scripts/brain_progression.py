#!/usr/bin/env python
"""Script for launch brain-progression."""

from brain_games import launcher_game
from brain_games.games import game_progression


def main():
    """Launch game_progression()."""
    launcher_game.launch_game(game_progression)


if __name__ == '__main__':
    main()
