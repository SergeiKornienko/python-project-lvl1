"""Question to player."""

import prompt


def welcome_user(question):
    """Ask question and get ansver.

    Args:
        question: str

    Returns:
        return: str
    """
    return prompt.string(question)
