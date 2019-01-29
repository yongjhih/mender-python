# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Release:
    """
    release name. 
    """
    name: Optional[str]
    """
    list of artifacts for this release. 
    """
    artifacts: Optional[Artifact]

