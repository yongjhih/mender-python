# -*- coding: future_fstrings -*-

import jsonpickle

from mender import Mender

import responses
import requests
import uuid
import os
import json
import pytest
from flo.echo_web_socket_server import EchoWebSocketServer
from unittest.mock import MagicMock

import ssl

import threading
from typing import Any, Callable, Dict, List, Optional, Union, NewType, Iterable, TypeVar

from _pytest.fixtures import SubRequest

@pytest.mark.asyncio
async def test_SimpleFloDevice_async_login(server):
    server.echo_data = '''{}'''

    res = '''{}''' # Mender.device_get(id = "")
    assert '''{}''' == res
