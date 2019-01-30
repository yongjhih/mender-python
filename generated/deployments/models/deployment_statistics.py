# -*- coding: future_fstrings -*-

from typing import Any, Dict, List, Optional, NewType, TypeVar
from dataclasses import dataclass

@dataclass
class DeploymentStatistics:
    success: int
    """
    Number of successful deployments.
    """
    pending: int
    """
    Number of pending deployments.
    """
    downloading: int
    """
    Number of deployments being downloaded.
    """
    rebooting: int
    """
    Number of deployments devices are rebooting into.
    """
    installing: int
    """
    Number of deployments devices being installed.
    """
    failure: int
    """
    Number of failed deployments.
    """
    noartifact: int
    """
    Do not have appropriate artifact for device type.
    """
    already_installed: int
    """
    Number of devices unaffected by upgrade, since they are already running the specified software version.
    """
    aborted: int
    """
    Number of deployments aborted by user.
    """

