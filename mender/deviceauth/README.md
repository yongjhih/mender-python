# Documentation for Device authentication

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://mender-device-auth:8080/api/management/v2/devauth*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**devices_count_get**](api/DefaultApi.md#devices_count_get) | **GET** /devices/count | Get a count of devices, optionally filtered by status.
*DefaultApi* | [**devices_get**](api/DefaultApi.md#devices_get) | **GET** /devices | Get a list of tenant's devices.
*DefaultApi* | [**devices_id_auth_aid_delete**](api/DefaultApi.md#devices_id_auth_aid_delete) | **DELETE** /devices/{id}/auth/{aid} | Remove the device authentication set
*DefaultApi* | [**devices_id_auth_aid_status_get**](api/DefaultApi.md#devices_id_auth_aid_status_get) | **GET** /devices/{id}/auth/{aid}/status | Get the device authentication set status
*DefaultApi* | [**devices_id_auth_aid_status_put**](api/DefaultApi.md#devices_id_auth_aid_status_put) | **PUT** /devices/{id}/auth/{aid}/status | Update the device authentication set status
*DefaultApi* | [**devices_id_delete**](api/DefaultApi.md#devices_id_delete) | **DELETE** /devices/{id} | Decommission device
*DefaultApi* | [**devices_id_get**](api/DefaultApi.md#devices_id_get) | **GET** /devices/{id} | Get a particular device.
*DefaultApi* | [**devices_post**](api/DefaultApi.md#devices_post) | **POST** /devices | Submit a preauthorized device.
*DefaultApi* | [**limits_max_devices_get**](api/DefaultApi.md#limits_max_devices_get) | **GET** /limits/max_devices | Obtain limit of accepted devices.
*DefaultApi* | [**tokens_id_delete**](api/DefaultApi.md#tokens_id_delete) | **DELETE** /tokens/{id} | Delete device token


<a name="documentation-for-models"></a>
## Documentation for Models

 - [models.AuthSet](models/AuthSet.md)
 - [models.Count](models/Count.md)
 - [models.Device](models/Device.md)
 - [models.Error](models/Error.md)
 - [models.IdentityData](models/IdentityData.md)
 - [models.Limit](models/Limit.md)
 - [models.PreAuthSet](models/PreAuthSet.md)
 - [models.Status](models/Status.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
