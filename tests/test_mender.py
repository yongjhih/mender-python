# -*- coding: future_fstrings -*-
import os

import aiohttp
import pytest

from mender import Mender


@pytest.mark.asyncio
async def test_login():
    async with Mender(base_url=os.environ["MENDER_URL"], session=aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))) as mender:
        token = await mender.login(os.environ["MENDER_USERNAME"], os.environ["MENDER_PASSWORD"])
        assert None != token
        devices = await mender.get_devices_paged()
        assert None != devices
        async for device in mender.get_devices():
            print(device)
            assert None != device
        #async for device in mender.get_devices(attributes={"hostname": 'xxx-ffffffffffff'}):
        #    print(device)
        #    assert None != device
