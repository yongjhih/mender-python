# coding: utf-8
# -*- coding: future_fstrings -*-

import asyncio
import ssl
import time
import uuid
from typing import Any, Dict, List, Optional, NewType, TypeVar, Iterable

import aiohttp
import jsonpickle
import jsontofu
from aiohttp import ClientResponse
from collections import AsyncIterable, AsyncGenerator

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
    def __init__(self, base_url: str, session: Optional[aiohttp.ClientSession] = None):
        self.base_url = base_url
        self.session = session if session else aiohttp.ClientSession()

    def url(self, url: str) -> str:
        return url if url.startswith('http://') or url.startswith('https://') else f'{self.base_url}/{url}'

    @staticmethod
    def stripDict(dictionary: Dict) -> Dict:
        return {k: v for k, v in dictionary.items() if v is not None}

    async def get(self, url: str, params: Optional[Dict] = None) -> ClientResponse:
        if params:
            return await self.session.get(url=self.url(url), params=Rests.stripDict(params))
        return await self.session.get(url=self.url(url))

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
    def __init__(self, base_url: str, session: Optional[aiohttp.ClientSession] = None):
        super().__init__(base_url, session if session else aiohttp.ClientSession())

    async def _get_devices_paged(self,
                                 page: Optional[int] = 1,
                                 per_page: Optional[int] = 10,
                                 sort: Optional[str] = None,
                                 has_group: Optional[bool] = None,
                                 attributes: Optional[Dict[str, Any]] = None) -> ClientResponse:
        """
        List devices

        GET /devices


        :param int page: Starting page.
        :param int per_page: Number of results per page.
        :param str sort: Supports sorting the device list by attribute values.  The parameter is formatted as a list of attribute names and sort directions, e.g.:  '?sort=attr1:asc, attr2:desc'  will sort by 'attr1' ascending, and then by 'attr2' descending. 'desc' is the default sort direction, and can be omitted.
        :param bool has_group: If present, limits the results only to devices assigned/not assigned to a group.

        :return: ClientResponse
        """
        if attributes != None:
            return await self.get(url=f"/inventory/devices",
                                  params={"page": page, "per_page": per_page, "sort": sort, "has_group": has_group,
                                          **attributes})
        else:
            return await self.get(url=f"/inventory/devices",
                                  params={"page": page, "per_page": per_page, "sort": sort, "has_group": has_group})

    async def get_devices_paged(self,
                                page: Optional[int] = 1,
                                per_page: Optional[int] = 10,
                                sort: Optional[str] = None,
                                has_group: Optional[bool] = None,
                                attributes: Optional[Dict[str, Any]] = None) -> Iterable[Device]:
        """
        List devices

        GET /devices


        :param int page: Starting page.
        :param int per_page: Number of results per page.
        :param str sort: Supports sorting the device list by attribute values.  The parameter is formatted as a list of attribute names and sort directions, e.g.:  '?sort=attr1:asc, attr2:desc'  will sort by 'attr1' ascending, and then by 'attr2' descending. 'desc' is the default sort direction, and can be omitted.
        :param bool has_group: If present, limits the results only to devices assigned/not assigned to a group.

        :return: Iterable[Device]
        """
        res = await self._get_devices_paged(page=page, per_page=per_page, sort=sort, has_group=has_group,
                                            attributes=attributes)
        return map(lambda x: jsontofu.decode(x, Device), await res.json())

    async def _get_devicesList(self,
                               page: Optional[int] = 1,
                               per_page: Optional[int] = 10,
                               sort: Optional[str] = None,
                               has_group: Optional[bool] = None,
                               attributes: Optional[Dict[str, Any]] = None
                               ) -> Iterable[List[Device]]:
        """
        List devices

        GET /devices

        Usage:

        :param int page: Starting page.
        :param int per_page: Number of results per page.
        :param str sort: Supports sorting the device list by attribute values.  The parameter is formatted as a list of attribute names and sort directions, e.g.:  '?sort=attr1:asc, attr2:desc'  will sort by 'attr1' ascending, and then by 'attr2' descending. 'desc' is the default sort direction, and can be omitted.
        :param bool has_group: If present, limits the results only to devices assigned/not assigned to a group.

        :return: Iterable[List[Device]]
        """
        _page = page
        res = await self._get_devices_paged(page=_page, per_page=per_page, sort=sort, has_group=has_group,
                                            attributes=attributes)
        _page = _page + 1
        yield res

        while True:
            if res.links and res.links.get('next'):
                res = await self.get(str(res.links.get('next').get('url')))
                yield res
            else:
                if await res.json():
                    res = await self._get_devices_paged(page=_page, per_page=per_page, sort=sort, has_group=has_group,
                                                        attributes=attributes)
                    _page = _page + 1
                    yield res
                else:
                    break

    async def get_devices(self,
                          page: Optional[int] = 1,
                          per_page: Optional[int] = 10,
                          sort: Optional[str] = None,
                          has_group: Optional[bool] = None,
                          attributes: Optional[Dict[str, Any]] = None
                          ) -> Iterable[Device]:
        """
        List devices

        GET /devices

        Usage:

        ```
        async for i in mender.get_devices():
            print(i)
        ```

        :param int page: Starting page.
        :param int per_page: Number of results per page.
        :param str sort: Supports sorting the device list by attribute values.  The parameter is formatted as a list of attribute names and sort directions, e.g.:  '?sort=attr1:asc, attr2:desc'  will sort by 'attr1' ascending, and then by 'attr2' descending. 'desc' is the default sort direction, and can be omitted.
        :param bool has_group: If present, limits the results only to devices assigned/not assigned to a group.

        :return: Iterable[Device]
        """
        async for res in self._get_devicesList(page=page, per_page=per_page, sort=sort, has_group=has_group,
                                               attributes=attributes):
            for device in await res.json():
                yield jsontofu.decode(device, Device)

    async def devices_id_delete(self, id: str) -> None:
        """
        Remove selected device

        DELETE /devices/{id}

        :param str id: Device identifier. (required)


        :return: None
        """
        return await self.delete(f"/inventory/devices/{id}")

    async def devices_id_get(self, id: str) -> Device:
        """
        Get a selected device

        GET /devices/{id}

        :param str id: Device identifier. (required)


        :return: Device
        """
        return await self.get(f"/inventory/devices/{id}")

    async def devices_id_group_get(self, id: str) -> Group:
        """
        Get a selected device&#39;s group

        GET /devices/{id}/group

        :param str id: Device identifier. (required)


        :return: Group
        """
        return await self.get(f"/inventory/devices/{id}/group")

    async def devices_id_group_name_delete(self, id: str, name: str) -> None:
        """
        Remove a device from a group

        DELETE /devices/{id}/group/{name}

        :param str id: Device identifier. (required)
        :param str name: Group name. (required)


        :return: None
        """
        return await self.delete(f"/inventory/devices/{id}/group/{name}")

    async def devices_id_group_put(self, id: str) -> None:
        """
        Add a device to a group

        PUT /devices/{id}/group

        :param str id: Device identifier. (required)


        :return: None
        """
        return await self.put(f"/inventory/devices/{id}/group")

    async def groups_get(self) -> List[str]:
        """
        List groups

        GET /groups



        :return: List[str]
        """
        return await self.get(f"/inventory/groups")

    async def groups_name_devices_get(self, name: str, page: Optional[int] = 1, per_page: Optional[int] = 10) -> List[
        str]:
        """
        List the devices belonging to a given group

        GET /groups/{name}/devices

        :param str name: Group name. (required)

        :param int page: Starting page.
        :param int per_page: Number of results per page.

        :return: List[str]
        """
        return await self.get(f"/inventory/groups/{name}/devices", {"page": page, "per_page": per_page, })

    async def _auth_login_post(self, username: str, password: str) -> None:
        """
        Log in to Mender

        POST /auth/login



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

        GET /settings



        :return: object
        """
        return await self.get(f"/useradm/settings")

    async def settings_post(self) -> None:
        """
        Set user settings

        POST /settings



        :return: None
        """
        return await self.post(f"/useradm/settings")

    async def users_get(self) -> List[User]:
        """
        List users

        GET /users



        :return: List[User]
        """
        return await self.get(f"/useradm/users")

    async def users_id_delete(self, id: str) -> None:
        """
        Remove user from the system

        DELETE /users/{id}

        :param str id: User id. (required)


        :return: None
        """
        return await self.delete(f"/useradm/users/{id}")

    async def users_id_get(self, id: str) -> User:
        """
        Get user information

        GET /users/{id}

        :param str id: User id. (required)


        :return: User
        """
        return await self.get(f"/useradm/users/{id}")

    async def users_id_put(self, id: str) -> None:
        """
        Update user information

        PUT /users/{id}

        :param str id: User id. (required)


        :return: None
        """
        return await self.put(f"/useradm/users/{id}")

    async def users_post(self) -> None:
        """
        Create user

        POST /users



        :return: None
        """
        return await self.post(f"/useradm/users")
