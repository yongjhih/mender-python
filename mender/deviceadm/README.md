# Documentation for Device admission

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://docker.mender.io/api/management/v1/admission*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**devices_get**](api/DefaultApi.md#devices_get) | **GET** /devices | List known device data sets
*DefaultApi* | [**devices_id_delete**](api/DefaultApi.md#devices_id_delete) | **DELETE** /devices/{id} | Remove device authentication data set
*DefaultApi* | [**devices_id_get**](api/DefaultApi.md#devices_id_get) | **GET** /devices/{id} | Get the details of a selected device authentication data set
*DefaultApi* | [**devices_id_put**](api/DefaultApi.md#devices_id_put) | **PUT** /devices/{id} | Submit a device authentication data set for admission
*DefaultApi* | [**devices_id_status_get**](api/DefaultApi.md#devices_id_status_get) | **GET** /devices/{id}/status | Check the admission status of a selected device authentication data set
*DefaultApi* | [**devices_id_status_put**](api/DefaultApi.md#devices_id_status_put) | **PUT** /devices/{id}/status | Update the admission status of a selected device
*DefaultApi* | [**devices_post**](api/DefaultApi.md#devices_post) | **POST** /devices | Submit a preauthorized device authentication data set


<a name="documentation-for-models"></a>
## Documentation for Models

 - [models.Attributes](models/Attributes.md)
 - [models.AuthSet](models/AuthSet.md)
 - [models.Device](models/Device.md)
 - [models.Error](models/Error.md)
 - [models.NewDevice](models/NewDevice.md)
 - [models.Status](models/Status.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
