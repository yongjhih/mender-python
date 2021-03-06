# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Artifact:
    name: str
    """
    
    """
    description: str
    """
    
    """
    device_types_compatible: List[str]
    """
    
    """
    id: str
    """
    
    """
    signed: Optional[bool] = None
    """
    Idicates if artifact is signed or not.
    """
    modified: datetime
    """
    Represents creation / last edition of any of the artifact properties. 
    """
    info: Optional[ArtifactInfo] = None
    """
    
    """
    updates: Optional[Update] = None
    """
    
    """

