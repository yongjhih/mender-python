# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class NewDevice:
    """
    The identity data of the device.
    """
    device_identity: str
    """
    Device public key
    """
    key: str
    """
    System-assigned device ID.
    """
    device_id: str

