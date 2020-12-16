#!/usr/bin/env python

from brain_games.cli import welcome_user

def intro(greet):
    print(greet)

def main():
    intro('Welcome to the Brain Games!')
    welcome_user()

if __name__ == '__main__':
    main()
