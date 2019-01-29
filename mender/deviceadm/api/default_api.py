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

    def __init__(self, base_url: str = 'https://docker.mender.io/api/management/v1/admission', session: aiohttp.ClientSession = aiohttp.ClientSession()):
        super().__init__(base_url, session)


    async def devices_get(self) -> List[Device]:
        """
        List known device data sets

        GET /devices


        :return: List[Device]
        """
        return await self.get(f"/devices")

    async def devices_id_delete(self, id: str) -> None:
        """
        Remove device authentication data set

        DELETE /devices/{id}

        :param str id: Device authentication data set identifier (required)

        :return: None
        """
        return await self.delete(f"/devices/{id}", {  "id": id,  } )

    async def devices_id_get(self, id: str) -> Device:
        """
        Get the details of a selected device authentication data set

        GET /devices/{id}

        :param str id: Device authentication data set identifier. (required)

        :return: Device
        """
        return await self.get(f"/devices/{id}", {  "id": id,  } )

    async def devices_id_put(self, id: str) -> None:
        """
        Submit a device authentication data set for admission

        PUT /devices/{id}

        :param str id: Device authentication data set identifier. (required)

        :return: None
        """
        return await self.put(f"/devices/{id}", {  "id": id,  } )

    async def devices_id_status_get(self, id: str) -> Status:
        """
        Check the admission status of a selected device authentication data set

        GET /devices/{id}/status

        :param str id: Device authentication data set identifier. (required)

        :return: Status
        """
        return await self.get(f"/devices/{id}/status", {  "id": id,  } )

    async def devices_id_status_put(self, id: str) -> Status:
        """
        Update the admission status of a selected device

        PUT /devices/{id}/status

        :param str id: Device authentication data set identifier. (required)

        :return: Status
        """
        return await self.put(f"/devices/{id}/status", {  "id": id,  } )

    async def devices_post(self) -> None:
        """
        Submit a preauthorized device authentication data set

        POST /devices


        :return: None
        """
        return await self.post(f"/devices")

