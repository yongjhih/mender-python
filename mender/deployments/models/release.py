# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Release:
    name: Optional[str] = None
    """
    release name. 
    """
    artifacts: Optional[Artifact] = None
    """
    list of artifacts for this release. 
    """

