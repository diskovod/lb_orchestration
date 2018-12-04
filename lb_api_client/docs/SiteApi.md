# swagger_client.SiteApi

All URIs are relative to *https://ces-remail-network-api.no.cie.cisco.com/v1/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_site**](SiteApi.md#create_site) | **POST** /sites | Add new site definition
[**get_all_sites**](SiteApi.md#get_all_sites) | **GET** /sites | Finds all supported sites
[**get_site**](SiteApi.md#get_site) | **GET** /sites/{id} | Get site by id


# **create_site**
> create_site(authorization=authorization, site=site)

Add new site definition

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
api_instance = swagger_client.SiteApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | A signed and valid Streamline IAM access token (optional)
site = swagger_client.SiteRequest() # SiteRequest | Filtering all sites by sites (optional)

try:
    # Add new site definition
    api_instance.create_site(authorization=authorization, site=site)
except ApiException as e:
    print("Exception when calling SiteApi->create_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A signed and valid Streamline IAM access token | [optional] 
 **site** | [**SiteRequest**](SiteRequest.md)| Filtering all sites by sites | [optional] 

### Return type

void (empty response body)

### Authorization

[jwtTokenValidate](../README.md#jwtTokenValidate)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sites**
> list[Site] get_all_sites(authorization=authorization)

Finds all supported sites

Finds all supported sites

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
api_instance = swagger_client.SiteApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | A signed and valid Streamline IAM access token (optional)

try:
    # Finds all supported sites
    api_response = api_instance.get_all_sites(authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_all_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A signed and valid Streamline IAM access token | [optional] 

### Return type

[**list[Site]**](Site.md)

### Authorization

[jwtTokenValidate](../README.md#jwtTokenValidate)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site**
> Site get_site(id, authorization=authorization)

Get site by id

Get site by id

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
api_instance = swagger_client.SiteApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | The site id that needs to be fetched
authorization = 'authorization_example' # str | A signed and valid Streamline IAM access token (optional)

try:
    # Get site by id
    api_response = api_instance.get_site(id, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->get_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The site id that needs to be fetched | 
 **authorization** | **str**| A signed and valid Streamline IAM access token | [optional] 

### Return type

[**Site**](Site.md)

### Authorization

[jwtTokenValidate](../README.md#jwtTokenValidate)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

