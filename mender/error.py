# -*- coding: future_fstrings -*-

from typing import Optional

from dataclasses import dataclass


@dataclass
class Error:
    error: Optional[str]
    """
    Description of the error.
    """
    request_id: Optional[str]
    """
    Request ID (same as in X-MEN-RequestID header).
    """

