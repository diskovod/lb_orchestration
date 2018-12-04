# swagger_client.VirtualserviceApi

All URIs are relative to *https://ces-remail-network-api.no.cie.cisco.com/v1/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_virtual_service**](VirtualserviceApi.md#add_virtual_service) | **POST** /virtualservice | Provision a new virtualservice to a specific site
[**delete_virtual_service**](VirtualserviceApi.md#delete_virtual_service) | **DELETE** /virtualservice/{id} | Delete an existing virtualservice by id
[**get_virtual_service**](VirtualserviceApi.md#get_virtual_service) | **GET** /virtualservice/{id} | Get a new virtualservice by id
[**modify_virtual_service**](VirtualserviceApi.md#modify_virtual_service) | **PUT** /virtualservice/{id} | Modify an existing virtualservice by id
[**virtualservice_get**](VirtualserviceApi.md#virtualservice_get) | **GET** /virtualservice | List all virtualservices in site


# **add_virtual_service**
> VirtualService add_virtual_service(virtualservice=virtualservice, authorization=authorization)

Provision a new virtualservice to a specific site

Provision ESA virtual service on a specific site. IPv4 address will be auto picked from IPAM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtTokenValidate
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.VirtualserviceApi(swagger_client.ApiClient(configuration))
virtualservice = swagger_client.VirtualServiceRequest() # VirtualServiceRequest | The virtual service to be created (optional)
authorization = 'authorization_example' # str | A signed and valid Streamline IAM access token (optional)

try:
    # Provision a new virtualservice to a specific site
    api_response = api_instance.add_virtual_service(virtualservice=virtualservice, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualserviceApi->add_virtual_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **virtualservice** | [**VirtualServiceRequest**](VirtualServiceRequest.md)| The virtual service to be created | [optional] 
 **authorization** | **str**| A signed and valid Streamline IAM access token | [optional] 

### Return type

[**VirtualService**](VirtualService.md)

### Authorization

[jwtTokenValidate](../README.md#jwtTokenValidate)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_service**
> delete_virtual_service(id)

Delete an existing virtualservice by id

Deletes ESA virtual service on a specific site by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtTokenValidate
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.VirtualserviceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The virtual service id that needs to be deleted

try:
    # Delete an existing virtualservice by id
    api_instance.delete_virtual_service(id)
except ApiException as e:
    print("Exception when calling VirtualserviceApi->delete_virtual_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The virtual service id that needs to be deleted | 

### Return type

void (empty response body)

### Authorization

[jwtTokenValidate](../README.md#jwtTokenValidate)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_service**
> VirtualService get_virtual_service(id, name=name, site_id=site_id)

Get a new virtualservice by id

Get a new virtualservice by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtTokenValidate
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.VirtualserviceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The virtual service id that needs to be fetched
name = 'name_example' # str | Customer name (optional)
site_id = 'site_id_example' # str | Site id for filter (optional)

try:
    # Get a new virtualservice by id
    api_response = api_instance.get_virtual_service(id, name=name, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualserviceApi->get_virtual_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The virtual service id that needs to be fetched | 
 **name** | **str**| Customer name | [optional] 
 **site_id** | **str**| Site id for filter | [optional] 

### Return type

[**VirtualService**](VirtualService.md)

### Authorization

[jwtTokenValidate](../README.md#jwtTokenValidate)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_virtual_service**
> VirtualService modify_virtual_service(id, virtualservice=virtualservice)

Modify an existing virtualservice by id

Modifies ESA virtual service on a speciic site by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtTokenValidate
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.VirtualserviceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The virtual service id that needs to be modified
virtualservice = swagger_client.VirtualServiceModifyRequest() # VirtualServiceModifyRequest | The virtual service to be modified (optional)

try:
    # Modify an existing virtualservice by id
    api_response = api_instance.modify_virtual_service(id, virtualservice=virtualservice)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualserviceApi->modify_virtual_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The virtual service id that needs to be modified | 
 **virtualservice** | [**VirtualServiceModifyRequest**](VirtualServiceModifyRequest.md)| The virtual service to be modified | [optional] 

### Return type

[**VirtualService**](VirtualService.md)

### Authorization

[jwtTokenValidate](../README.md#jwtTokenValidate)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualservice_get**
> list[VirtualService] virtualservice_get(authorization=authorization, site=site)

List all virtualservices in site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwtTokenValidate
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.VirtualserviceApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | A signed and valid Streamline IAM access token (optional)
site = 'site_example' # str | Filtering all sites by sites (optional)

try:
    # List all virtualservices in site
    api_response = api_instance.virtualservice_get(authorization=authorization, site=site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualserviceApi->virtualservice_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A signed and valid Streamline IAM access token | [optional] 
 **site** | **str**| Filtering all sites by sites | [optional] 

### Return type

[**list[VirtualService]**](VirtualService.md)

### Authorization

[jwtTokenValidate](../README.md#jwtTokenValidate)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

