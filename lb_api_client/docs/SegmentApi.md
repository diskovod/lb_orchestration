# swagger_client.SegmentApi

All URIs are relative to *https://ces-remail-network-api.no.cie.cisco.com/v1/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_next_segment**](SegmentApi.md#get_next_segment) | **GET** /segment/getNextSegment | gets next Segment
[**get_segments**](SegmentApi.md#get_segments) | **GET** /segment | Finds supported segments


# **get_next_segment**
> list[Segment] get_next_segment(authorization=authorization, algorithm=algorithm, site_id=site_id)

gets next Segment

gets next Segment to use for provisioning

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
api_instance = swagger_client.SegmentApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | A signed and valid Streamline IAM access token (optional)
algorithm = ['algorithm_example'] # list[str] | Algorithm to use to get next segment. Options available are least virtual services in a segment or least loaded segment. Defaults to least_vs when this query isnt provided (optional)
site_id = 'site_id_example' # str | filter based on site_id (optional)

try:
    # gets next Segment
    api_response = api_instance.get_next_segment(authorization=authorization, algorithm=algorithm, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentApi->get_next_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A signed and valid Streamline IAM access token | [optional] 
 **algorithm** | [**list[str]**](str.md)| Algorithm to use to get next segment. Options available are least virtual services in a segment or least loaded segment. Defaults to least_vs when this query isnt provided | [optional] 
 **site_id** | **str**| filter based on site_id | [optional] 

### Return type

[**list[Segment]**](Segment.md)

### Authorization

[jwtTokenValidate](../README.md#jwtTokenValidate)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segments**
> list[Segment] get_segments(authorization=authorization, site_id=site_id)

Finds supported segments

Finds supported segments

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
api_instance = swagger_client.SegmentApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | A signed and valid Streamline IAM access token (optional)
site_id = 'site_id_example' # str | filter based on site id, if site id isnt provided fetches all segments (optional)

try:
    # Finds supported segments
    api_response = api_instance.get_segments(authorization=authorization, site_id=site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentApi->get_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| A signed and valid Streamline IAM access token | [optional] 
 **site_id** | **str**| filter based on site id, if site id isnt provided fetches all segments | [optional] 

### Return type

[**list[Segment]**](Segment.md)

### Authorization

[jwtTokenValidate](../README.md#jwtTokenValidate)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

