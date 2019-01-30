# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Error:
    error: Optional[str] = None
    """
    Description of the error
    """

