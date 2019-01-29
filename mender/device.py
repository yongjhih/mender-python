# -*- coding: future_fstrings -*-

from typing import Optional

from dataclasses import dataclass

from .attribute import Attribute


@dataclass
class Device:
    """
    Mender-assigned unique ID.
    """
    id: Optional[str]
    """
    Timestamp of the most recent attribute update.
    """
    updated_ts: Optional[str]
    """
    A list of attribute descriptors.
    """
    attributes: Optional[Attribute]

