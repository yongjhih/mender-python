# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Attributes:
    mac: Optional[str] = None
    """
    MAC address.
    """
    sku: Optional[str] = None
    """
    Stock keeping unit.
    """
    sn: Optional[str] = None
    """
    Serial number.
    """

