# Mender

## Usage

```py
mender = Mender(base_url = 'https://docker.mender.io/api/management/v1/inventory')
devices = await mender.devices_get()
```

## Device inventory

### API Endpoints

All URIs are relative to *https://docker.mender.io/api/management/v1/inventory*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Mender* | **devices_get** | **GET** /devices | List devices
*Mender* | **devices_id_delete** | **DELETE** /devices/{id} | Remove selected device
*Mender* | **devices_id_get** | **GET** /devices/{id} | Get a selected device
*Mender* | **devices_id_group_get** | **GET** /devices/{id}/group | Get a selected device's group
*Mender* | **devices_id_group_name_delete** | **DELETE** /devices/{id}/group/{name} | Remove a device from a group
*Mender* | **devices_id_group_put** | **PUT** /devices/{id}/group | Add a device to a group
*Mender* | **groups_get** | **GET** /groups | List groups
*Mender* | **groups_name_devices_get** | **GET** /groups/{name}/devices | List the devices belonging to a given group
