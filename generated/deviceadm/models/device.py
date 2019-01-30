# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class Device:
    id: str
    """
    Authentication data set identifier.
    """
    device_id: str
    """
    System assigned device identifier.
    """
    device_identity: str
    """
    Identity data
    """
    key: str
    """
    Device public key
    """
    status: str
    """
    Status of the admission process for device authentication data set
    """
    attributes: Attributes
    """
    
    """
    request_time: str
    """
    Server-side timestamp of the request reception.
    """

