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

    def __init__(self, base_url: str = https://docker.mender.io/api/management/v1/deployments):
        super().__init__(base_url)


    async def artifacts_get(self) -> List[Artifact]:
        """
        List known artifacts

        method: GET
        path: /artifacts


        :return: List[Artifact]
        """
        return await self.get(f"/artifacts")

    async def artifacts_id_delete(self, id: str) -> None:
        """
        Delete the artifact

        method: DELETE
        path: /artifacts/{id}

        :param str id: Artifact identifier. (required)

        :return: None
        """
        return await self.delete(f"/artifacts/{id}", {  "id": id,  } )

    async def artifacts_id_download_get(self, id: str) -> ArtifactLink:
        """
        Get the download link of a selected artifact

        method: GET
        path: /artifacts/{id}/download

        :param str id: Artifact identifier. (required)

        :return: ArtifactLink
        """
        return await self.get(f"/artifacts/{id}/download", {  "id": id,  } )

    async def artifacts_id_get(self, id: str) -> Artifact:
        """
        Get the details of a selected artifact

        method: GET
        path: /artifacts/{id}

        :param str id: Artifact identifier. (required)

        :return: Artifact
        """
        return await self.get(f"/artifacts/{id}", {  "id": id,  } )

    async def artifacts_id_put(self, id: str) -> None:
        """
        Update description of a selected artifact

        method: PUT
        path: /artifacts/{id}

        :param str id: Artifact identifier. (required)

        :return: None
        """
        return await self.put(f"/artifacts/{id}", {  "id": id,  } )

    async def artifacts_post(self) -> None:
        """
        Upload mender artifact

        method: POST
        path: /artifacts


        :return: None
        """
        return await self.post(f"/artifacts")

    async def deployments_deployment_id_devices_device_id_log_get(self, deployment_id: str, device_id: str) -> None:
        """
        Get the log of a selected device&#39;s deployment

        method: GET
        path: /deployments/{deployment_id}/devices/{device_id}/log

        :param str deployment_id: Deployment identifier. (required)
        :param str device_id: Device identifier. (required)

        :return: None
        """
        return await self.get(f"/deployments/{deployment_id}/devices/{device_id}/log", {  "deployment_id": deployment_id,  "device_id": device_id,  } )

    async def deployments_deployment_id_devices_get(self, deployment_id: str) -> List[Device]:
        """
        List devices of a deployment

        method: GET
        path: /deployments/{deployment_id}/devices

        :param str deployment_id: Deployment identifier. (required)

        :return: List[Device]
        """
        return await self.get(f"/deployments/{deployment_id}/devices", {  "deployment_id": deployment_id,  } )

    async def deployments_deployment_id_statistics_get(self, deployment_id: str) -> DeploymentStatistics:
        """
        Get the statistics of a selected deployment

        method: GET
        path: /deployments/{deployment_id}/statistics

        :param str deployment_id: Deployment identifier (required)

        :return: DeploymentStatistics
        """
        return await self.get(f"/deployments/{deployment_id}/statistics", {  "deployment_id": deployment_id,  } )

    async def deployments_deployment_id_status_put(self, deployment_id: str) -> None:
        """
        Abort the deployment

        method: PUT
        path: /deployments/{deployment_id}/status

        :param str deployment_id: Deployment identifier. (required)

        :return: None
        """
        return await self.put(f"/deployments/{deployment_id}/status", {  "deployment_id": deployment_id,  } )

    async def deployments_devices_id_delete(self, id: str) -> None:
        """
        Remove device from all deployments

        method: DELETE
        path: /deployments/devices/{id}

        :param str id: System wide device identifier (required)

        :return: None
        """
        return await self.delete(f"/deployments/devices/{id}", {  "id": id,  } )

    async def deployments_get(self) -> List[Deployment]:
        """
        Find all deployments

        method: GET
        path: /deployments


        :return: List[Deployment]
        """
        return await self.get(f"/deployments")

    async def deployments_id_get(self, id: str) -> Deployment:
        """
        Get the details of a selected deployment

        method: GET
        path: /deployments/{id}

        :param str id: Deployment identifier. (required)

        :return: Deployment
        """
        return await self.get(f"/deployments/{id}", {  "id": id,  } )

    async def deployments_post(self) -> None:
        """
        Create a deployment

        method: POST
        path: /deployments


        :return: None
        """
        return await self.post(f"/deployments")

    async def deployments_releases_get(self) -> List[Release]:
        """
        List releases

        method: GET
        path: /deployments/releases


        :return: List[Release]
        """
        return await self.get(f"/deployments/releases")

    async def limits_storage_get(self) -> StorageLimit:
        """
        Get storage limit and current storage usage

        method: GET
        path: /limits/storage


        :return: StorageLimit
        """
        return await self.get(f"/limits/storage")

