# openapi_client.VoiceprintApi

All URIs are relative to *https://vpc.speakin.mobi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ctcdasr**](VoiceprintApi.md#ctcdasr) | **POST** /cloudapi/v1beta/voiceprint/ctcdasr | 
[**delete**](VoiceprintApi.md#delete) | **POST** /cloudapi/v1beta/voiceprint/delete | 
[**query**](VoiceprintApi.md#query) | **POST** /cloudapi/v1beta/voiceprint/query | 
[**register**](VoiceprintApi.md#register) | **POST** /cloudapi/v1beta/voiceprint/register | 
[**threshold**](VoiceprintApi.md#threshold) | **POST** /cloudapi/v1beta/voiceprint/threshold | 
[**vadcheck**](VoiceprintApi.md#vadcheck) | **POST** /cloudapi/v1beta/voiceprint/vadcheck | 
[**verify**](VoiceprintApi.md#verify) | **POST** /cloudapi/v1beta/voiceprint/verify | 
[**verify1ton**](VoiceprintApi.md#verify1ton) | **POST** /cloudapi/v1beta/voiceprint/verify1ton | 
[**verify_multi**](VoiceprintApi.md#verify_multi) | **POST** /cloudapi/v1beta/voiceprint/verify_multi | 
[**verifytopn**](VoiceprintApi.md#verifytopn) | **POST** /cloudapi/v1beta/voiceprint/verifytopn | 


# **ctcdasr**
> RespVoiceprintCtcdasrResponse ctcdasr(voiceprint_ctcdasr_request=voiceprint_ctcdasr_request)



数字asr

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.VoiceprintApi()
voiceprint_ctcdasr_request = openapi_client.VoiceprintCtcdasrRequest() # VoiceprintCtcdasrRequest |  (optional)

try:
    api_response = api_instance.ctcdasr(voiceprint_ctcdasr_request=voiceprint_ctcdasr_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceprintApi->ctcdasr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceprint_ctcdasr_request** | [**VoiceprintCtcdasrRequest**](VoiceprintCtcdasrRequest.md)|  | [optional] 

### Return type

[**RespVoiceprintCtcdasrResponse**](RespVoiceprintCtcdasrResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> RespVoiceprintDeleteResponse delete(voiceprint_delete_request=voiceprint_delete_request)



声纹查询

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



声纹查询

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



声纹注册

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



查询阈值

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

# **vadcheck**
> RespVoiceprintVadcheckResponse vadcheck(voiceprint_vadcheck_request=voiceprint_vadcheck_request)



VAD检测

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.VoiceprintApi()
voiceprint_vadcheck_request = openapi_client.VoiceprintVadcheckRequest() # VoiceprintVadcheckRequest |  (optional)

try:
    api_response = api_instance.vadcheck(voiceprint_vadcheck_request=voiceprint_vadcheck_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceprintApi->vadcheck: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceprint_vadcheck_request** | [**VoiceprintVadcheckRequest**](VoiceprintVadcheckRequest.md)|  | [optional] 

### Return type

[**RespVoiceprintVadcheckResponse**](RespVoiceprintVadcheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify**
> RespVoiceprintVerifyResponse verify(voiceprint_verify_request=voiceprint_verify_request)



声纹验证

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



声纹验证

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

# **verify_multi**
> RespVoiceprintVerifyMultiResponse verify_multi(voiceprint_verify_multi_request=voiceprint_verify_multi_request)



声纹验证1对多

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.VoiceprintApi()
voiceprint_verify_multi_request = openapi_client.VoiceprintVerifyMultiRequest() # VoiceprintVerifyMultiRequest |  (optional)

try:
    api_response = api_instance.verify_multi(voiceprint_verify_multi_request=voiceprint_verify_multi_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceprintApi->verify_multi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceprint_verify_multi_request** | [**VoiceprintVerifyMultiRequest**](VoiceprintVerifyMultiRequest.md)|  | [optional] 

### Return type

[**RespVoiceprintVerifyMultiResponse**](RespVoiceprintVerifyMultiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verifytopn**
> RespVoiceprinttopnVerifyResponse verifytopn(voiceprinttopn_verify_request=voiceprinttopn_verify_request)



声纹验证

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

