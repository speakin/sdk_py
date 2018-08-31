# openapi_client.VoiceprintApi

All URIs are relative to *http://192.168.1.157:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](VoiceprintApi.md#delete) | **POST** /cloudapi/v1beta/voiceprint/delete | 
[**query**](VoiceprintApi.md#query) | **POST** /cloudapi/v1beta/voiceprint/query | 
[**register**](VoiceprintApi.md#register) | **POST** /cloudapi/v1beta/voiceprint/register | 
[**threshold**](VoiceprintApi.md#threshold) | **POST** /cloudapi/v1beta/voiceprint/threshold | 
[**verify**](VoiceprintApi.md#verify) | **POST** /cloudapi/v1beta/voiceprint/verify | 
[**verify1ton**](VoiceprintApi.md#verify1ton) | **POST** /cloudapi/v1beta/voiceprint/verify1ton | 
[**verifytopn**](VoiceprintApi.md#verifytopn) | **POST** /cloudapi/v1beta/voiceprint/verifytopn | 


# **delete**
> RespVoiceprintDeleteResponse delete(voiceprint_delete_request=voiceprint_delete_request)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.VoiceprintApi()
voiceprint_delete_request = openapi_client.VoiceprintDeleteRequest() # VoiceprintDeleteRequest |  (optional)

try:
    api_response = api_instance.delete(voiceprint_delete_request=voiceprint_delete_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceprintApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceprint_delete_request** | [**VoiceprintDeleteRequest**](VoiceprintDeleteRequest.md)|  | [optional] 

### Return type

[**RespVoiceprintDeleteResponse**](RespVoiceprintDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query**
> RespVoiceprintQueryResponse query(voiceprint_query_request=voiceprint_query_request)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.VoiceprintApi()
voiceprint_query_request = openapi_client.VoiceprintQueryRequest() # VoiceprintQueryRequest |  (optional)

try:
    api_response = api_instance.query(voiceprint_query_request=voiceprint_query_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceprintApi->query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceprint_query_request** | [**VoiceprintQueryRequest**](VoiceprintQueryRequest.md)|  | [optional] 

### Return type

[**RespVoiceprintQueryResponse**](RespVoiceprintQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> RespVoiceprintRegisterResponse register(voiceprint_register_request=voiceprint_register_request)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.VoiceprintApi()
voiceprint_register_request = openapi_client.VoiceprintRegisterRequest() # VoiceprintRegisterRequest |  (optional)

try:
    api_response = api_instance.register(voiceprint_register_request=voiceprint_register_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceprintApi->register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceprint_register_request** | [**VoiceprintRegisterRequest**](VoiceprintRegisterRequest.md)|  | [optional] 

### Return type

[**RespVoiceprintRegisterResponse**](RespVoiceprintRegisterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **threshold**
> RespVoiceprintThresholdResponse threshold(voiceprint_threshold_request=voiceprint_threshold_request)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.VoiceprintApi()
voiceprint_threshold_request = openapi_client.VoiceprintThresholdRequest() # VoiceprintThresholdRequest |  (optional)

try:
    api_response = api_instance.threshold(voiceprint_threshold_request=voiceprint_threshold_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceprintApi->threshold: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceprint_threshold_request** | [**VoiceprintThresholdRequest**](VoiceprintThresholdRequest.md)|  | [optional] 

### Return type

[**RespVoiceprintThresholdResponse**](RespVoiceprintThresholdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify**
> RespVoiceprintVerifyResponse verify(voiceprint_verify_request=voiceprint_verify_request)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.VoiceprintApi()
voiceprint_verify_request = openapi_client.VoiceprintVerifyRequest() # VoiceprintVerifyRequest |  (optional)

try:
    api_response = api_instance.verify(voiceprint_verify_request=voiceprint_verify_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceprintApi->verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceprint_verify_request** | [**VoiceprintVerifyRequest**](VoiceprintVerifyRequest.md)|  | [optional] 

### Return type

[**RespVoiceprintVerifyResponse**](RespVoiceprintVerifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify1ton**
> RespVoiceprint1tonVerifyResponse verify1ton(voiceprint1ton_verify_request=voiceprint1ton_verify_request)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.VoiceprintApi()
voiceprint1ton_verify_request = openapi_client.Voiceprint1tonVerifyRequest() # Voiceprint1tonVerifyRequest |  (optional)

try:
    api_response = api_instance.verify1ton(voiceprint1ton_verify_request=voiceprint1ton_verify_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceprintApi->verify1ton: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceprint1ton_verify_request** | [**Voiceprint1tonVerifyRequest**](Voiceprint1tonVerifyRequest.md)|  | [optional] 

### Return type

[**RespVoiceprint1tonVerifyResponse**](RespVoiceprint1tonVerifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verifytopn**
> RespVoiceprinttopnVerifyResponse verifytopn(voiceprinttopn_verify_request=voiceprinttopn_verify_request)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.VoiceprintApi()
voiceprinttopn_verify_request = openapi_client.VoiceprinttopnVerifyRequest() # VoiceprinttopnVerifyRequest |  (optional)

try:
    api_response = api_instance.verifytopn(voiceprinttopn_verify_request=voiceprinttopn_verify_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceprintApi->verifytopn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceprinttopn_verify_request** | [**VoiceprinttopnVerifyRequest**](VoiceprinttopnVerifyRequest.md)|  | [optional] 

### Return type

[**RespVoiceprinttopnVerifyResponse**](RespVoiceprinttopnVerifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

