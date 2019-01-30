# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Device:
    id: Optional[str] = None
    """
    Mender assigned Device ID.
    """
    identity_data: Optional[IdentityData] = None
    """
    
    """
    status: Optional[str] = None
    """
    
    """
    created_ts: Optional[str] = None
    """
    Created timestamp
    """
    updated_ts: Optional[str] = None
    """
    Updated timestamp
    """
    auth_sets: Optional[AuthSet] = None
    """
    
    """
    decommissioning: Optional[bool] = None
    """
    Devices that are part of ongoing decomissioning process will return True
    """

