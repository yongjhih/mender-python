# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Attribute:
    name: str
    """
    A human readable, unique attribute ID, e.g. &#39;device_type&#39;, &#39;ip_addr&#39;, &#39;cpu_load&#39;, etc. 
    """
    description: Optional[str] = None
    """
    Attribute description.
    """
    value: str
    """
    The current value of the attribute.  Attribute type is implicit, inferred from the JSON type.  Supported types: number, string, array of numbers, array of strings. Mixed arrays are not allowed. 
    """

