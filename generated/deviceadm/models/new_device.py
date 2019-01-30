# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class NewDevice:
    device_identity: str
    """
    The identity data of the device.
    """
    key: str
    """
    Device public key
    """
    device_id: str
    """
    System-assigned device ID.
    """

