# coding: utf-8
# -*- coding: future_fstrings -*-

import asyncio
import ssl
import time
import uuid
from typing import Any, Dict, List, Optional, NewType, TypeVar

import aiohttp
import jsonpickle
import jsontofu
from aiohttp.client import ClientSession
from aiohttp.client_ws import ClientWebSocketResponse
from aiohttp.http_websocket import WSMessage
from dataclasses import dataclass
from requests.exceptions import HTTPError

class Rests():
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = aiohttp.ClientSession()

    def url(url: str) -> str:
        return url if url.startswith('http://') or url.startswith('https://') else f'{self.base_url}/{url}'

    async def get(self, url: str):
        async with self.session.get(url(url)) as response:
            return await response

    async def post(self, url: str, data: Optional[Dict]):
        async with self.session.post(url(url)) as response:
            return await response

    async def put(self, url: str, data: Optional[Dict]):
        async with self.session.put(url(url)) as response:
            return await response

    async def delete(self, url: str):
        async with self.session.delete(url(url)) as response:
            return await response

    async def head(self, url: str):
        async with self.session.head(url(url)) as response:
            return await response

    async def options(self, url: str):
        async with self.session.head(url(url)) as response:
            return await response

    async def patch(self, url: str, data: Optional[Dict]):
        async with self.session.head(url(url)) as response:
            return await response


class DefaultApi(Rests):

    def __init__(self, base_url: str = http://mender-device-auth:8080/api/management/v2/devauth):
        super().__init__(base_url)


    async def devices_count_get(self) -> Count:
        """
        Get a count of devices, optionally filtered by status.

        method: GET
        path: /devices/count


        :return: Count
        """
        return await self.get(f"/devices/count")

    async def devices_get(self) -> List[Device]:
        """
        Get a list of tenant&#39;s devices.

        method: GET
        path: /devices


        :return: List[Device]
        """
        return await self.get(f"/devices")

    async def devices_id_auth_aid_delete(self, id: str, aid: str) -> None:
        """
        Remove the device authentication set

        method: DELETE
        path: /devices/{id}/auth/{aid}

        :param str id: Device identifier. (required)
        :param str aid: Authentication data set identifier. (required)

        :return: None
        """
        return await self.delete(f"/devices/{id}/auth/{aid}", {  "id": id,  "aid": aid,  } )

    async def devices_id_auth_aid_status_get(self, id: str, aid: str) -> Status:
        """
        Get the device authentication set status

        method: GET
        path: /devices/{id}/auth/{aid}/status

        :param str id: Device identifier. (required)
        :param str aid: Authentication data set identifier. (required)

        :return: Status
        """
        return await self.get(f"/devices/{id}/auth/{aid}/status", {  "id": id,  "aid": aid,  } )

    async def devices_id_auth_aid_status_put(self, id: str, aid: str) -> None:
        """
        Update the device authentication set status

        method: PUT
        path: /devices/{id}/auth/{aid}/status

        :param str id: Device identifier. (required)
        :param str aid: Authentication data set identifier. (required)

        :return: None
        """
        return await self.put(f"/devices/{id}/auth/{aid}/status", {  "id": id,  "aid": aid,  } )

    async def devices_id_delete(self, id: str) -> None:
        """
        Decommission device

        method: DELETE
        path: /devices/{id}

        :param str id: Device identifier. (required)

        :return: None
        """
        return await self.delete(f"/devices/{id}", {  "id": id,  } )

    async def devices_id_get(self, id: str) -> Device:
        """
        Get a particular device.

        method: GET
        path: /devices/{id}

        :param str id: Device identifier (required)

        :return: Device
        """
        return await self.get(f"/devices/{id}", {  "id": id,  } )

    async def devices_post(self) -> None:
        """
        Submit a preauthorized device.

        method: POST
        path: /devices


        :return: None
        """
        return await self.post(f"/devices")

    async def limits_max_devices_get(self) -> Limit:
        """
        Obtain limit of accepted devices.

        method: GET
        path: /limits/max_devices


        :return: Limit
        """
        return await self.get(f"/limits/max_devices")

    async def tokens_id_delete(self, id: str) -> None:
        """
        Delete device token

        method: DELETE
        path: /tokens/{id}

        :param str id: Unique token identifier('jti'). (required)

        :return: None
        """
        return await self.delete(f"/tokens/{id}", {  "id": id,  } )

