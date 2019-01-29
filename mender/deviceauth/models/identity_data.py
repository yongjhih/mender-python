# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class IdentityData:
    """
    MAC address.
    """
    mac: Optional[str] = None
    """
    Stock keeping unit.
    """
    sku: Optional[str] = None
    """
    Serial number.
    """
    sn: Optional[str] = None

