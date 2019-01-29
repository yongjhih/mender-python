# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Device:
    """
    Mender-assigned unique ID.
    """
    id: Optional[str]
    """
    Timestamp of the most recent attribute update.
    """
    updated_ts: Optional[str]
    """
    A list of attribute descriptors.
    """
    attributes: Optional[Attribute]

