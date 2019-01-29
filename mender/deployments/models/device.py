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
    finished: Optional[datetime] = None
    """
    
    """
    status: str
    """
    
    """
    created: Optional[datetime] = None
    """
    
    """
    device_type: Optional[str] = None
    """
    Availability of the device&#39;s deployment log.
    """
    log: bool
    """
    State reported by device
    """
    state: Optional[str] = None
    """
    Additional state information
    """
    substate: Optional[str] = None

