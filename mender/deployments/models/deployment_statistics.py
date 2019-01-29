# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class DeploymentStatistics:
    """
    Number of successful deployments.
    """
    success: int
    """
    Number of pending deployments.
    """
    pending: int
    """
    Number of deployments being downloaded.
    """
    downloading: int
    """
    Number of deployments devices are rebooting into.
    """
    rebooting: int
    """
    Number of deployments devices being installed.
    """
    installing: int
    """
    Number of failed deployments.
    """
    failure: int
    """
    Do not have appropriate artifact for device type.
    """
    noartifact: int
    """
    Number of devices unaffected by upgrade, since they are already running the specified software version.
    """
    already_installed: int
    """
    Number of deployments aborted by user.
    """
    aborted: int

