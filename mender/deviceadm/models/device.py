# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Device:
    """
    Authentication data set identifier.
    """
    id: str
    """
    System assigned device identifier.
    """
    device_id: str
    """
    Identity data
    """
    device_identity: str
    """
    Device public key
    """
    key: str
    """
    Status of the admission process for device authentication data set
    """
    status: str
    """
    
    """
    attributes: Attributes
    """
    Server-side timestamp of the request reception.
    """
    request_time: str

