# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Device:
    """
    Device identifier.
    """
    id: str
    """
    
    """
    finished: Optional[datetime]
    """
    
    """
    status: str
    """
    
    """
    created: Optional[datetime]
    """
    
    """
    device_type: Optional[str]
    """
    Availability of the device&#39;s deployment log.
    """
    log: bool
    """
    State reported by device
    """
    state: Optional[str]
    """
    Additional state information
    """
    substate: Optional[str]

