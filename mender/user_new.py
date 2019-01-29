# -*- coding: future_fstrings -*-

from dataclasses import dataclass

@dataclass
class UserNew:
    email: str
    """
    A unique email address. Invalid characters are non-ascii and &#39;+&#39;.
    """
    password: str
    """
    Password.
    """

