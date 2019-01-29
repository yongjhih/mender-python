# -*- coding: future_fstrings -*-

from typing import Optional

from dataclasses import dataclass


@dataclass
class Error:
    error: Optional[str] = None
    """
    Description of the error.
    """
    request_id: Optional[str] = None
    """
    Request ID (same as in X-MEN-RequestID header).
    """

