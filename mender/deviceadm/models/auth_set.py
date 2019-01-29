# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class AuthSet:
    """
    The identity data of the device.
    """
    device_identity: str
    """
    Device public key.
    """
    key: str

