# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Error:
    """
    Description of the error.
    """
    error: Optional[str] = None
    """
    Request ID (same as in X-MEN-RequestID header).
    """
    request_id: Optional[str] = None

