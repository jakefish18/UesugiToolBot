"""
Function for security like password hashing and etc.
"""

import secrets

import bcrypt

from core import settings


def create_token() -> str:
    """
    Generating random token.

    Parameters:
        token_lenght: int - token lenght in bytes count. So actually token lenght will token_lenght * 2 symbols.

    Returning:
        token: str - generated token.
    """
    token = secrets.token_hex(settings.ACCESS_TOKEN_LENGHT_IN_BYTES)
    return token


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifying password.
    Calculating hash with salt again.
    If hashes are equal, then password is correct.

    Parameters:
        plain_password: str - password to check.
        hashed_password: str - hashed password to compare.

    Returns:
        is_right: bool - boolean that entered password hash is equal with hash.
    """
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


def get_password_hash(plain_password: str) -> str:
    """
    Generating password hash from plain password.

    Parameters:
        plain_password: str - clean password.

    Returns:
        password_hash: str - password hash.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")