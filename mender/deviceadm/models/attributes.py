# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Attributes:
    """
    MAC address.
    """
    mac: Optional[str]
    """
    Stock keeping unit.
    """
    sku: Optional[str]
    """
    Serial number.
    """
    sn: Optional[str]

