# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class StorageLimit:
    limit: int
    """
    Storage limit in bytes. If set to 0 - there is no limit for storage. 
    """
    usage: int
    """
    Current storage usage in bytes. 
    """

