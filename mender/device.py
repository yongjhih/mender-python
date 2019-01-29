# -*- coding: future_fstrings -*-

from typing import Optional, List

from dataclasses import dataclass

from .attribute import Attribute


@dataclass
class Device:
    id: Optional[str] = None
    """
    Mender-assigned unique ID.
    """
    updated_ts: Optional[str] = None
    """
    Timestamp of the most recent attribute update.
    """
    attributes: Optional[List[Attribute]] = None
    """
    A list of attribute descriptors.
    """

