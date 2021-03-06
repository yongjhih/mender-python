# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Update:
    type_info: Optional[ArtifactTypeInfo] = None
    """
    
    """
    files: Optional[UpdateFile] = None
    """
    
    """
    meta_data: Optional[] = None
    """
    meta_data is an object of unknown structure as this is dependent of update type (also custom defined by user) 
    """

