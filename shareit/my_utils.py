"""
This module provides a utility function for generating secure
random tokens.
"""

import secrets
import string


def generate_token(length=7):
    """
    Generates a secure random token consisting of letters and digits.

    The token is generated using the `secrets` module, which provides
    cryptographically secure random numbers.
    The default length of the token is 7 characters, but this can be
    adjusted by passing a different length as an argument.

    Args:
        length (int, optional): The length of the generated token.
        Defaults to 7.

    Returns:
        str: A string representing the generated token, consisting
        of random letters and digits.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))
