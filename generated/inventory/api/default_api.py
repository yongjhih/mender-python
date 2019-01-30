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

    def __init__(self, base_url: str = 'https://docker.mender.io/api/management/v1/inventory', session: aiohttp.ClientSession = aiohttp.ClientSession()):
        super().__init__(base_url, session)


    async def devices_get(self, page: Optional[int] = 1, per_page: Optional[int] = 10, sort: Optional[str] = None, has_group: Optional[bool] = None) -> List[Device]:
        """
        List devices

        GET /devices


        :param int page: Starting page.
        :param int per_page: Number of results per page.
        :param str sort: Supports sorting the device list by attribute values.  The parameter is formatted as a list of attribute names and sort directions, e.g.:  '?sort=attr1:asc, attr2:desc'  will sort by 'attr1' ascending, and then by 'attr2' descending. 'desc' is the default sort direction, and can be omitted. 
        :param bool has_group: If present, limits the results only to devices assigned/not assigned to a group.

        :return: List[Device]
        """
        return await self.get(f"/devices", {  "page": page,  "per_page": per_page,  "sort": sort,  "has_group": has_group,  } )

    async def devices_id_delete(self, id: str) -> None:
        """
        Remove selected device

        DELETE /devices/{id}

        :param str id: Device identifier. (required)


        :return: None
        """
        return await self.delete(f"/devices/{id}")

    async def devices_id_get(self, id: str) -> Device:
        """
        Get a selected device

        GET /devices/{id}

        :param str id: Device identifier. (required)


        :return: Device
        """
        return await self.get(f"/devices/{id}")

    async def devices_id_group_get(self, id: str) -> Group:
        """
        Get a selected device&#39;s group

        GET /devices/{id}/group

        :param str id: Device identifier. (required)


        :return: Group
        """
        return await self.get(f"/devices/{id}/group")

    async def devices_id_group_name_delete(self, id: str, name: str) -> None:
        """
        Remove a device from a group

        DELETE /devices/{id}/group/{name}

        :param str id: Device identifier. (required)
        :param str name: Group name. (required)


        :return: None
        """
        return await self.delete(f"/devices/{id}/group/{name}")

    async def devices_id_group_put(self, id: str) -> None:
        """
        Add a device to a group

        PUT /devices/{id}/group

        :param str id: Device identifier. (required)


        :return: None
        """
        return await self.put(f"/devices/{id}/group")

    async def groups_get(self) -> List[str]:
        """
        List groups

        GET /groups



        :return: List[str]
        """
        return await self.get(f"/groups")

    async def groups_name_devices_get(self, name: str, page: Optional[int] = 1, per_page: Optional[int] = 10) -> List[str]:
        """
        List the devices belonging to a given group

        GET /groups/{name}/devices

        :param str name: Group name. (required)

        :param int page: Starting page.
        :param int per_page: Number of results per page.

        :return: List[str]
        """
        return await self.get(f"/groups/{name}/devices", {  "page": page,  "per_page": per_page,  } )

