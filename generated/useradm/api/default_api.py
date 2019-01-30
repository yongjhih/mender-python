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

    def __init__(self, base_url: str = 'https://docker.mender.io/api/management/v1/useradm', session: aiohttp.ClientSession = aiohttp.ClientSession()):
        super().__init__(base_url, session)


    async def auth_login_post(self) -> None:
        """
        Log in to Mender

        POST /auth/login



        :return: None
        """
        return await self.post(f"/auth/login")

    async def settings_get(self) -> object:
        """
        Get user settings

        GET /settings



        :return: object
        """
        return await self.get(f"/settings")

    async def settings_post(self) -> None:
        """
        Set user settings

        POST /settings



        :return: None
        """
        return await self.post(f"/settings")

    async def users_get(self) -> List[User]:
        """
        List users

        GET /users



        :return: List[User]
        """
        return await self.get(f"/users")

    async def users_id_delete(self, id: str) -> None:
        """
        Remove user from the system

        DELETE /users/{id}

        :param str id: User id. (required)


        :return: None
        """
        return await self.delete(f"/users/{id}")

    async def users_id_get(self, id: str) -> User:
        """
        Get user information

        GET /users/{id}

        :param str id: User id. (required)


        :return: User
        """
        return await self.get(f"/users/{id}")

    async def users_id_put(self, id: str) -> None:
        """
        Update user information

        PUT /users/{id}

        :param str id: User id. (required)


        :return: None
        """
        return await self.put(f"/users/{id}")

    async def users_post(self) -> None:
        """
        Create user

        POST /users



        :return: None
        """
        return await self.post(f"/users")

