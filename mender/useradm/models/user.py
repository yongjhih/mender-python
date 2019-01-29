# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class User:
    """
    A unique email address.
    """
    email: str
    """
    User Id.
    """
    id: str
    """
    Server-side timestamp of the user creation. 
    """
    created_ts: Optional[datetime]
    """
    Server-side timestamp of the last user information update. 
    """
    updated_ts: Optional[datetime]

