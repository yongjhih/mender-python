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

#from .* import *

class JwtAuth(aiohttp.helpers.BasicAuth):
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.jwt = f"Bearer {self.access_token}"

    def encode(self) -> str:
        return self.jwt


class Rests():
    def __init__(self, base_url: str, session: aiohttp.ClientSession = aiohttp.ClientSession()):
        self.base_url = base_url
        self.session = session

    def url(self, url: str) -> str:
        return url if url.startswith('http://') or url.startswith('https://') else f'{self.base_url}/{url}'

    async def get(self, url: str) -> ClientResponse:
        return await self.session.get(self.url(url))

    async def post(self, url: str, data: Optional[Dict] = None) -> ClientResponse:
        return await self.session.post(url=self.url(url), data=data)

    async def put(self, url: str, data: Optional[Dict] = None) -> ClientResponse:
        return await self.session.put(url=self.url(url), data=data)

    async def delete(self, url: str) -> ClientResponse:
        return await self.session.delete(self.url(url))

    async def head(self, url: str) -> ClientResponse:
        return await self.session.head(self.url(url))

    async def options(self, url: str) -> ClientResponse:
        return await self.session.head(self.url(url))

    async def patch(self, url: str, data: Optional[Dict] = None) -> ClientResponse:
        return await self.session.head(url=self.url(url), data=data)


class DefaultApi(Rests):

    def __init__(self, base_url: str = 'http://mender-device-auth:8080/api/management/v2/devauth', session: aiohttp.ClientSession = aiohttp.ClientSession()):
        super().__init__(base_url, session)


    async def devices_count_get(self, status: Optional[str] = None) -> Count:
        """
        Get a count of devices, optionally filtered by status.

        GET /devices/count


        :param str status: Device status filter, one of 'pending', 'accepted', 'rejected'. Default is 'all devices'. 

        :return: Count
        """
        return await self.get(f"/devices/count", {  "status": status,  } )

    async def devices_get(self, status: Optional[str] = None, page: Optional[int] = 1, per_page: Optional[int] = 20) -> List[Device]:
        """
        Get a list of tenant&#39;s devices.

        GET /devices


        :param str status: Device status filter. If not specified, all devices are listed. 
        :param int page: Results page number
        :param int per_page: Number of results per page

        :return: List[Device]
        """
        return await self.get(f"/devices", {  "status": status,  "page": page,  "per_page": per_page,  } )

    async def devices_id_auth_aid_delete(self, id: str, aid: str) -> None:
        """
        Remove the device authentication set

        DELETE /devices/{id}/auth/{aid}

        :param str id: Device identifier. (required)
        :param str aid: Authentication data set identifier. (required)


        :return: None
        """
        return await self.delete(f"/devices/{id}/auth/{aid}")

    async def devices_id_auth_aid_status_get(self, id: str, aid: str) -> Status:
        """
        Get the device authentication set status

        GET /devices/{id}/auth/{aid}/status

        :param str id: Device identifier. (required)
        :param str aid: Authentication data set identifier. (required)


        :return: Status
        """
        return await self.get(f"/devices/{id}/auth/{aid}/status")

    async def devices_id_auth_aid_status_put(self, id: str, aid: str) -> None:
        """
        Update the device authentication set status

        PUT /devices/{id}/auth/{aid}/status

        :param str id: Device identifier. (required)
        :param str aid: Authentication data set identifier. (required)


        :return: None
        """
        return await self.put(f"/devices/{id}/auth/{aid}/status")

    async def devices_id_delete(self, id: str) -> None:
        """
        Decommission device

        DELETE /devices/{id}

        :param str id: Device identifier. (required)


        :return: None
        """
        return await self.delete(f"/devices/{id}")

    async def devices_id_get(self, id: str) -> Device:
        """
        Get a particular device.

        GET /devices/{id}

        :param str id: Device identifier (required)


        :return: Device
        """
        return await self.get(f"/devices/{id}")

    async def devices_post(self) -> None:
        """
        Submit a preauthorized device.

        POST /devices



        :return: None
        """
        return await self.post(f"/devices")

    async def limits_max_devices_get(self) -> Limit:
        """
        Obtain limit of accepted devices.

        GET /limits/max_devices



        :return: Limit
        """
        return await self.get(f"/limits/max_devices")

    async def tokens_id_delete(self, id: str) -> None:
        """
        Delete device token

        DELETE /tokens/{id}

        :param str id: Unique token identifier('jti'). (required)


        :return: None
        """
        return await self.delete(f"/tokens/{id}")

