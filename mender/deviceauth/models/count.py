# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Count:
    """
    The count of requested items.
    """
    count: Optional[int]

