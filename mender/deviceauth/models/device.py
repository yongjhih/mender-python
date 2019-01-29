# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Device:
    """
    Mender assigned Device ID.
    """
    id: Optional[str] = None
    """
    
    """
    identity_data: Optional[IdentityData] = None
    """
    
    """
    status: Optional[str] = None
    """
    Created timestamp
    """
    created_ts: Optional[str] = None
    """
    Updated timestamp
    """
    updated_ts: Optional[str] = None
    """
    
    """
    auth_sets: Optional[AuthSet] = None
    """
    Devices that are part of ongoing decomissioning process will return True
    """
    decommissioning: Optional[bool] = None

