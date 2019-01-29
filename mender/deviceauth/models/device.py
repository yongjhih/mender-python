# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Device:
    """
    Mender assigned Device ID.
    """
    id: Optional[str]
    """
    
    """
    identity_data: Optional[IdentityData]
    """
    
    """
    status: Optional[str]
    """
    Created timestamp
    """
    created_ts: Optional[str]
    """
    Updated timestamp
    """
    updated_ts: Optional[str]
    """
    
    """
    auth_sets: Optional[AuthSet]
    """
    Devices that are part of ongoing decomissioning process will return True
    """
    decommissioning: Optional[bool]

