# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Device:
    id: Optional[str] = None
    """
    Mender-assigned unique ID.
    """
    updated_ts: Optional[str] = None
    """
    Timestamp of the most recent attribute update.
    """
    attributes: Optional[Attribute] = None
    """
    A list of attribute descriptors.
    """

