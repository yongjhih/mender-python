# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class User:
    email: str
    """
    A unique email address.
    """
    id: str
    """
    User Id.
    """
    created_ts: Optional[datetime] = None
    """
    Server-side timestamp of the user creation. 
    """
    updated_ts: Optional[datetime] = None
    """
    Server-side timestamp of the last user information update. 
    """

