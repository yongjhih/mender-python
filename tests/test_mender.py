# -*- coding: future_fstrings -*-
import os

import aiohttp
import pytest

from mender import Mender


@pytest.mark.asyncio
async def test_login():
    #mender = Mender(base_url=os.environ["MENDER_URL"], session=aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)))
    mender = Mender()
    token = await mender.login(os.environ["MENDER_PASSWORD"], os.environ["MENDER_PASSWORD"])
    assert None != token
