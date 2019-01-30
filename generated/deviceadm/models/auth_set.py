# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class AuthSet:
    device_identity: str
    """
    The identity data of the device.
    """
    key: str
    """
    Device public key.
    """

