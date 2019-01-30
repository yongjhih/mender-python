# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
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

