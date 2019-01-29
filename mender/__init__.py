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
from aiohttp import ClientResponse

from .device import Device
from .group import Group
from .attribute import Attribute
from .error import Error
from .user import User
from .user_new import UserNew
from .user_update import UserUpdate

class JwtAuth(aiohttp.helpers.BasicAuth):
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.jwt = f"Bearer {self.access_token}"

    def encode(self) -> str:
        return self.jwt

class Rests():
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = aiohttp.ClientSession()

    def url(self, url: str) -> str:
        return url if url.startswith('http://') or url.startswith('https://') else f'{self.base_url}/{url}'

    async def get(self, url: str) -> ClientResponse:
        async with self.session.get(url(url)) as response:
            return await response

    async def post(self, url: str, data: Optional[Dict]) -> ClientResponse:
        async with self.session.post(url(url), data) as response:
            return await response

    async def put(self, url: str, data: Optional[Dict]) -> ClientResponse:
        async with self.session.put(url(url), data) as response:
            return await response

    async def delete(self, url: str) -> ClientResponse:
        async with self.session.delete(url(url)) as response:
            return await response

    async def head(self, url: str) -> ClientResponse:
        async with self.session.head(url(url)) as response:
            return await response

    async def options(self, url: str) -> ClientResponse:
        async with self.session.head(url(url)) as response:
            return await response

    async def patch(self, url: str, data: Optional[Dict]) -> ClientResponse:
        async with self.session.head(url(url), data) as response:
            return await response


class Mender(Rests):
    def __init__(self, base_url: str = 'https://docker.mender.io/api/management/v1'):
        super().__init__(base_url)

    async def devices_get(self) -> List[Device]:
        """
        List devices

        method: GET
        path: /devices


        :return: List[Device]
        """
        res = await self.get(f"/inventory/devices")
        return jsontofu.decode(res.json(), List[Device])

    async def devices_id_delete(self, id: str) -> None:
        """
        Remove selected device

        method: DELETE
        path: /devices/{id}

        :param str id: Device identifier. (required)

        :return: None
        """
        return await self.delete(f"/inventory/devices/{id}", {"id": id, })

    async def devices_id_get(self, id: str) -> Device:
        """
        Get a selected device

        method: GET
        path: /devices/{id}

        :param str id: Device identifier. (required)

        :return: Device
        """
        return await self.get(f"/inventory/devices/{id}", {"id": id, })

    async def devices_id_group_get(self, id: str) -> Group:
        """
        Get a selected device&#39;s group

        method: GET
        path: /devices/{id}/group

        :param str id: Device identifier. (required)

        :return: Group
        """
        return await self.get(f"/inventory/devices/{id}/group", {"id": id, })

    async def devices_id_group_name_delete(self, id: str, name: str) -> None:
        """
        Remove a device from a group

        method: DELETE
        path: /devices/{id}/group/{name}

        :param str id: Device identifier. (required)
        :param str name: Group name. (required)

        :return: None
        """
        return await self.delete(f"/inventory/devices/{id}/group/{name}", {"id": id, "name": name, })

    async def devices_id_group_put(self, id: str) -> None:
        """
        Add a device to a group

        method: PUT
        path: /devices/{id}/group

        :param str id: Device identifier. (required)

        :return: None
        """
        return await self.put(f"/inventory/devices/{id}/group", {"id": id, })

    async def groups_get(self) -> List[str]:
        """
        List groups

        method: GET
        path: /groups


        :return: List[str]
        """
        return await self.get(f"/inventory/groups")

    async def groups_name_devices_get(self, name: str) -> List[str]:
        """
        List the devices belonging to a given group

        method: GET
        path: /groups/{name}/devices

        :param str name: Group name. (required)

        :return: List[str]
        """
        return await self.get(f"/inventory/groups/{name}/devices", {"name": name, })

    async def _auth_login_post(self, username: str, password: str) -> ClientResponse:
        """
        Log in to Mender

        method: POST
        path: /auth/login

        :return: None
        """
        self.session._default_auth = (username, password)
        return await self.post(f"/useradm/auth/login")

    async def login(self, username: str, password: str) -> str:
        res = await self._auth_login_post(username, password)
        token = await res.text()
        self.session._default_auth = JwtAuth(token)
        return token

    async def settings_get(self) -> object:
        """
        Get user settings

        method: GET
        path: /settings


        :return: object
        """
        return await self.get(f"/useradm/settings")

    async def settings_post(self) -> None:
        """
        Set user settings

        method: POST
        path: /settings


        :return: None
        """
        return await self.post(f"/useradm/settings")

    async def users_get(self) -> List[User]:
        """
        List users

        method: GET
        path: /users


        :return: List[User]
        """
        return await self.get(f"/useradm/users")

    async def users_id_delete(self, id: str) -> None:
        """
        Remove user from the system

        method: DELETE
        path: /users/{id}

        :param str id: User id. (required)

        :return: None
        """
        return await self.delete(f"/useradm/users/{id}", {  "id": id,  } )

    async def users_id_get(self, id: str) -> User:
        """
        Get user information

        method: GET
        path: /users/{id}

        :param str id: User id. (required)

        :return: User
        """
        return await self.get(f"/useradm/users/{id}", {  "id": id,  } )

    async def users_id_put(self, id: str) -> None:
        """
        Update user information

        method: PUT
        path: /users/{id}

        :param str id: User id. (required)

        :return: None
        """
        return await self.put(f"/useradm/users/{id}", {  "id": id,  } )

    async def users_post(self) -> None:
        """
        Create user

        method: POST
        path: /users


        :return: None
        """
        return await self.post(f"/useradm/users")
