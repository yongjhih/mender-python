# -*- coding: future_fstrings -*-

import jsonpickle

from mender import Mender

import responses
import requests
import uuid
import os
import json
import pytest
from unittest.mock import MagicMock

import ssl

from typing import Any, Callable, Dict, List, Optional, Union, NewType, Iterable, TypeVar

from _pytest.fixtures import SubRequest

@pytest.mark.asyncio
async def test_login():
    res = '''{}''' # Mender.device_get(id = "")
    assert '''{}''' == res
