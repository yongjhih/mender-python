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

    def __init__(self, base_url: str = 'https://docker.mender.io/api/management/v1/deployments', session: aiohttp.ClientSession = aiohttp.ClientSession()):
        super().__init__(base_url, session)


    async def artifacts_get(self) -> List[Artifact]:
        """
        List known artifacts

        GET /artifacts



        :return: List[Artifact]
        """
        return await self.get(f"/artifacts")

    async def artifacts_id_delete(self, id: str) -> None:
        """
        Delete the artifact

        DELETE /artifacts/{id}

        :param str id: Artifact identifier. (required)


        :return: None
        """
        return await self.delete(f"/artifacts/{id}")

    async def artifacts_id_download_get(self, id: str) -> ArtifactLink:
        """
        Get the download link of a selected artifact

        GET /artifacts/{id}/download

        :param str id: Artifact identifier. (required)


        :return: ArtifactLink
        """
        return await self.get(f"/artifacts/{id}/download")

    async def artifacts_id_get(self, id: str) -> Artifact:
        """
        Get the details of a selected artifact

        GET /artifacts/{id}

        :param str id: Artifact identifier. (required)


        :return: Artifact
        """
        return await self.get(f"/artifacts/{id}")

    async def artifacts_id_put(self, id: str) -> None:
        """
        Update description of a selected artifact

        PUT /artifacts/{id}

        :param str id: Artifact identifier. (required)


        :return: None
        """
        return await self.put(f"/artifacts/{id}")

    async def artifacts_post(self) -> None:
        """
        Upload mender artifact

        POST /artifacts



        :return: None
        """
        return await self.post(f"/artifacts")

    async def deployments_deployment_id_devices_device_id_log_get(self, deployment_id: str, device_id: str) -> None:
        """
        Get the log of a selected device&#39;s deployment

        GET /deployments/{deployment_id}/devices/{device_id}/log

        :param str deployment_id: Deployment identifier. (required)
        :param str device_id: Device identifier. (required)


        :return: None
        """
        return await self.get(f"/deployments/{deployment_id}/devices/{device_id}/log")

    async def deployments_deployment_id_devices_get(self, deployment_id: str) -> List[Device]:
        """
        List devices of a deployment

        GET /deployments/{deployment_id}/devices

        :param str deployment_id: Deployment identifier. (required)


        :return: List[Device]
        """
        return await self.get(f"/deployments/{deployment_id}/devices")

    async def deployments_deployment_id_statistics_get(self, deployment_id: str) -> DeploymentStatistics:
        """
        Get the statistics of a selected deployment

        GET /deployments/{deployment_id}/statistics

        :param str deployment_id: Deployment identifier (required)


        :return: DeploymentStatistics
        """
        return await self.get(f"/deployments/{deployment_id}/statistics")

    async def deployments_deployment_id_status_put(self, deployment_id: str) -> None:
        """
        Abort the deployment

        PUT /deployments/{deployment_id}/status

        :param str deployment_id: Deployment identifier. (required)


        :return: None
        """
        return await self.put(f"/deployments/{deployment_id}/status")

    async def deployments_devices_id_delete(self, id: str) -> None:
        """
        Remove device from all deployments

        DELETE /deployments/devices/{id}

        :param str id: System wide device identifier (required)


        :return: None
        """
        return await self.delete(f"/deployments/devices/{id}")

    async def deployments_get(self, status: Optional[str] = None, search: Optional[str] = None, page: Optional[int] = 1, per_page: Optional[int] = 20, created_before: Optional[int] = None, created_after: Optional[int] = None) -> List[Deployment]:
        """
        Find all deployments

        GET /deployments


        :param str status: Deployment status filter.
        :param str search: Deployment name or description filter.
        :param int page: Results page number
        :param int per_page: Number of results per page
        :param int created_before: List only deployments created before and equal to Unix timestamp (UTC)
        :param int created_after: List only deployments created after and equal to Unix timestamp (UTC)

        :return: List[Deployment]
        """
        return await self.get(f"/deployments", {  "status": status,  "search": search,  "page": page,  "per_page": per_page,  "created_before": created_before,  "created_after": created_after,  } )

    async def deployments_id_get(self, id: str) -> Deployment:
        """
        Get the details of a selected deployment

        GET /deployments/{id}

        :param str id: Deployment identifier. (required)


        :return: Deployment
        """
        return await self.get(f"/deployments/{id}")

    async def deployments_post(self) -> None:
        """
        Create a deployment

        POST /deployments



        :return: None
        """
        return await self.post(f"/deployments")

    async def deployments_releases_get(self, name: Optional[str] = None) -> List[Release]:
        """
        List releases

        GET /deployments/releases


        :param str name: Release name filter.

        :return: List[Release]
        """
        return await self.get(f"/deployments/releases", {  "name": name,  } )

    async def limits_storage_get(self) -> StorageLimit:
        """
        Get storage limit and current storage usage

        GET /limits/storage



        :return: StorageLimit
        """
        return await self.get(f"/limits/storage")

