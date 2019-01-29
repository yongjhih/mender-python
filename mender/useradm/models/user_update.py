# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class UserUpdate:
    """
    A unique email address.
    """
    email: Optional[str]
    """
    Password.
    """
    password: Optional[str]

