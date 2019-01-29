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

    def __init__(self, base_url: str = https://docker.mender.io/api/management/v1/inventory):
        super().__init__(base_url)


    async def devices_get(self) -> List[Device]:
        """
        List devices

        method: GET
        path: /devices


        :return: List[Device]
        """
        return await self.get(f"/devices")

    async def devices_id_delete(self, id: str) -> None:
        """
        Remove selected device

        method: DELETE
        path: /devices/{id}

        :param str id: Device identifier. (required)

        :return: None
        """
        return await self.delete(f"/devices/{id}", {  "id": id,  } )

    async def devices_id_get(self, id: str) -> Device:
        """
        Get a selected device

        method: GET
        path: /devices/{id}

        :param str id: Device identifier. (required)

        :return: Device
        """
        return await self.get(f"/devices/{id}", {  "id": id,  } )

    async def devices_id_group_get(self, id: str) -> Group:
        """
        Get a selected device&#39;s group

        method: GET
        path: /devices/{id}/group

        :param str id: Device identifier. (required)

        :return: Group
        """
        return await self.get(f"/devices/{id}/group", {  "id": id,  } )

    async def devices_id_group_name_delete(self, id: str, name: str) -> None:
        """
        Remove a device from a group

        method: DELETE
        path: /devices/{id}/group/{name}

        :param str id: Device identifier. (required)
        :param str name: Group name. (required)

        :return: None
        """
        return await self.delete(f"/devices/{id}/group/{name}", {  "id": id,  "name": name,  } )

    async def devices_id_group_put(self, id: str) -> None:
        """
        Add a device to a group

        method: PUT
        path: /devices/{id}/group

        :param str id: Device identifier. (required)

        :return: None
        """
        return await self.put(f"/devices/{id}/group", {  "id": id,  } )

    async def groups_get(self) -> List[str]:
        """
        List groups

        method: GET
        path: /groups


        :return: List[str]
        """
        return await self.get(f"/groups")

    async def groups_name_devices_get(self, name: str) -> List[str]:
        """
        List the devices belonging to a given group

        method: GET
        path: /groups/{name}/devices

        :param str name: Group name. (required)

        :return: List[str]
        """
        return await self.get(f"/groups/{name}/devices", {  "name": name,  } )

