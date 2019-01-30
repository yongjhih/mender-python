# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Device:
    id: str
    """
    Device identifier.
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
    
    """
    log: bool
    """
    Availability of the device&#39;s deployment log.
    """
    state: Optional[str] = None
    """
    State reported by device
    """
    substate: Optional[str] = None
    """
    Additional state information
    """

