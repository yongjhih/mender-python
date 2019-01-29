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


class Mender(Rests):
    def __init__(self, base_url: str, session: aiohttp.ClientSession = aiohttp.ClientSession()):
        super().__init__(base_url, session)

    async def devices_get(self) -> List[Device]:
        """
        List devices

        GET /devices


        :return: List[Device]
        """
        res = await self.get(f"/inventory/devices")
        return list(map(lambda x: jsontofu.decode(x, Device), await res.json()))

    async def devices_id_delete(self, id: str) -> None:
        """
        Remove selected device

        DELETE /devices/{id}

        :param str id: Device identifier. (required)

        :return: None
        """
        return await self.delete(f"/inventory/devices/{id}", {  "id": id,  } )

    async def devices_id_get(self, id: str) -> Device:
        """
        Get a selected device

        GET /devices/{id}

        :param str id: Device identifier. (required)

        :return: Device
        """
        return await self.get(f"/inventory/devices/{id}", {  "id": id,  } )

    async def devices_id_group_get(self, id: str) -> Group:
        """
        Get a selected device&#39;s group

        GET /devices/{id}/group

        :param str id: Device identifier. (required)

        :return: Group
        """
        return await self.get(f"/inventory/devices/{id}/group", {  "id": id,  } )

    async def devices_id_group_name_delete(self, id: str, name: str) -> None:
        """
        Remove a device from a group

        DELETE /devices/{id}/group/{name}

        :param str id: Device identifier. (required)
        :param str name: Group name. (required)

        :return: None
        """
        return await self.delete(f"/inventory/devices/{id}/group/{name}", {  "id": id,  "name": name,  } )

    async def devices_id_group_put(self, id: str) -> None:
        """
        Add a device to a group

        PUT /devices/{id}/group

        :param str id: Device identifier. (required)

        :return: None
        """
        return await self.put(f"/inventory/devices/{id}/group", {  "id": id,  } )

    async def groups_get(self) -> List[str]:
        """
        List groups

        GET /groups


        :return: List[str]
        """
        return await self.get(f"/inventory/groups")

    async def groups_name_devices_get(self, name: str) -> List[str]:
        """
        List the devices belonging to a given group

        GET /groups/{name}/devices

        :param str name: Group name. (required)

        :return: List[str]
        """
        return await self.get(f"/inventory/groups/{name}/devices", {  "name": name,  } )


    async def _auth_login_post(self, username: str, password: str) -> ClientResponse:
        """
        Log in to Mender

        method: POST
        path: /auth/login

        :return: None
        """
        self.session._default_auth = aiohttp.helpers.BasicAuth(username, password)
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
        return await self.delete(f"/useradm/users/{id}", {"id": id, })

    async def users_id_get(self, id: str) -> User:
        """
        Get user information

        method: GET
        path: /users/{id}

        :param str id: User id. (required)

        :return: User
        """
        return await self.get(f"/useradm/users/{id}", {"id": id, })

    async def users_id_put(self, id: str) -> None:
        """
        Update user information

        method: PUT
        path: /users/{id}

        :param str id: User id. (required)

        :return: None
        """
        return await self.put(f"/useradm/users/{id}", {"id": id, })

    async def users_post(self) -> None:
        """
        Create user

        method: POST
        path: /users


        :return: None
        """
        return await self.post(f"/useradm/users")
