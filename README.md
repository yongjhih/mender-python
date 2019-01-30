# Mender

## Usage

```py
mender = Mender(base_url = 'https://docker.mender.io/api/management/v1')

# List devices on page 1
devices = await mender.get_devices_paged(page=1)
print(devices)

# List all devices
async for device in mender.get_devices():
    print(device)

# Filter all devices by attributes
async for device in mender.get_devices(attributes={"hostname": 'xxx-ffffffffffff'}):
    print(device)
```

## Installation

Using pip:

```sh
pip install mender
```

Using pipenv:

```sh
pipenv install mender
```

## Deployment

```sh
pipenv run python3 setup.py sdist bdist_wheel
pipenv run twine upload dist/*
```

## Device inventory

`/inventory`

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

## User administration and authentication

`/useradm`

### API Endpoints

All URIs are relative to *https://docker.mender.io/api/management/v1/useradm*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Mender* | **auth_login_post** | **POST** /auth/login | Log in to Mender
*Mender* | **settings_get** | **GET** /settings | Get user settings
*Mender* | **settings_post** | **POST** /settings | Set user settings
*Mender* | **users_get** | **GET** /users | List users
*Mender* | **users_id_delete** | **DELETE** /users/{id} | Remove user from the system
*Mender* | **users_id_get** | **GET** /users/{id} | Get user information
*Mender* | **users_id_put** | **PUT** /users/{id} | Update user information
*Mender* | **users_post** | **POST** /users | Create user

## References

* https://github.com/yongjhih/mender.js
* https://github.com/yongjhih/openapi-generator/tree/mender/modules/openapi-generator/src/main/resources/python-typing-client
