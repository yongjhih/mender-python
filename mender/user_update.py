# -*- coding: future_fstrings -*-

from typing import Optional

from dataclasses import dataclass


@dataclass
class UserUpdate:
    email: Optional[str] = None
    """
    A unique email address.
    """
    password: Optional[str] = None
    """
    Password.
    """

