# -*- coding: future_fstrings -*-

from typing import Optional

from dataclasses import dataclass

from .attribute import Attribute


@dataclass
class Device:
    id: Optional[str]
    """
    Mender-assigned unique ID.
    """
    updated_ts: Optional[str]
    """
    Timestamp of the most recent attribute update.
    """
    attributes: Optional[Attribute]
    """
    A list of attribute descriptors.
    """

