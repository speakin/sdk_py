# openapi_client.StorageApi

All URIs are relative to *http://192.168.1.157:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download**](StorageApi.md#download) | **GET** /cloudapi/v1beta/storage/download | 
[**upload**](StorageApi.md#upload) | **POST** /cloudapi/v1beta/storage/upload | 


# **download**
> file download(bucket, key)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.StorageApi()
bucket = 'bucket_example' # str | 
key = 123 # str | 

try:
    api_response = api_instance.download(bucket, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **key** | **str**|  | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> CallUploadResponse upload(bucket, type, duration_ms, timestamp, body=body)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.StorageApi()
bucket = 'bucket_example' # str | 
type = wav # str | 
duration_ms = 0 # int | 
timestamp = 123 # int | 
body = '/path/to/file' # file |  (optional)

try:
    api_response = api_instance.upload(bucket, type, duration_ms, timestamp, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **type** | **str**|  | 
 **duration_ms** | **int**|  | 
 **timestamp** | **int**|  | 
 **body** | **file**|  | [optional] 

### Return type

[**CallUploadResponse**](CallUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

