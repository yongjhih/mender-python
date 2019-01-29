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

    def __init__(self, base_url: str = https://docker.mender.io/api/management/v1/admission):
        super().__init__(base_url)


    async def devices_get(self) -> List[Device]:
        """
        List known device data sets

        method: GET
        path: /devices


        :return: List[Device]
        """
        return await self.get(f"/devices")

    async def devices_id_delete(self, id: str) -> None:
        """
        Remove device authentication data set

        method: DELETE
        path: /devices/{id}

        :param str id: Device authentication data set identifier (required)

        :return: None
        """
        return await self.delete(f"/devices/{id}", {  "id": id,  } )

    async def devices_id_get(self, id: str) -> Device:
        """
        Get the details of a selected device authentication data set

        method: GET
        path: /devices/{id}

        :param str id: Device authentication data set identifier. (required)

        :return: Device
        """
        return await self.get(f"/devices/{id}", {  "id": id,  } )

    async def devices_id_put(self, id: str) -> None:
        """
        Submit a device authentication data set for admission

        method: PUT
        path: /devices/{id}

        :param str id: Device authentication data set identifier. (required)

        :return: None
        """
        return await self.put(f"/devices/{id}", {  "id": id,  } )

    async def devices_id_status_get(self, id: str) -> Status:
        """
        Check the admission status of a selected device authentication data set

        method: GET
        path: /devices/{id}/status

        :param str id: Device authentication data set identifier. (required)

        :return: Status
        """
        return await self.get(f"/devices/{id}/status", {  "id": id,  } )

    async def devices_id_status_put(self, id: str) -> Status:
        """
        Update the admission status of a selected device

        method: PUT
        path: /devices/{id}/status

        :param str id: Device authentication data set identifier. (required)

        :return: Status
        """
        return await self.put(f"/devices/{id}/status", {  "id": id,  } )

    async def devices_post(self) -> None:
        """
        Submit a preauthorized device authentication data set

        method: POST
        path: /devices


        :return: None
        """
        return await self.post(f"/devices")

