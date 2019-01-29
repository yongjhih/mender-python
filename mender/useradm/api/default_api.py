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

    def __init__(self, base_url: str = https://docker.mender.io/api/management/v1/useradm):
        super().__init__(base_url)


    async def auth_login_post(self) -> None:
        """
        Log in to Mender

        method: POST
        path: /auth/login


        :return: None
        """
        return await self.post(f"/auth/login")

    async def settings_get(self) -> object:
        """
        Get user settings

        method: GET
        path: /settings


        :return: object
        """
        return await self.get(f"/settings")

    async def settings_post(self) -> None:
        """
        Set user settings

        method: POST
        path: /settings


        :return: None
        """
        return await self.post(f"/settings")

    async def users_get(self) -> List[User]:
        """
        List users

        method: GET
        path: /users


        :return: List[User]
        """
        return await self.get(f"/users")

    async def users_id_delete(self, id: str) -> None:
        """
        Remove user from the system

        method: DELETE
        path: /users/{id}

        :param str id: User id. (required)

        :return: None
        """
        return await self.delete(f"/users/{id}", {  "id": id,  } )

    async def users_id_get(self, id: str) -> User:
        """
        Get user information

        method: GET
        path: /users/{id}

        :param str id: User id. (required)

        :return: User
        """
        return await self.get(f"/users/{id}", {  "id": id,  } )

    async def users_id_put(self, id: str) -> None:
        """
        Update user information

        method: PUT
        path: /users/{id}

        :param str id: User id. (required)

        :return: None
        """
        return await self.put(f"/users/{id}", {  "id": id,  } )

    async def users_post(self) -> None:
        """
        Create user

        method: POST
        path: /users


        :return: None
        """
        return await self.post(f"/users")

