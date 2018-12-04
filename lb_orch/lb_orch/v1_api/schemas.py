# -*- coding: utf-8 -*-

import six
from jsonschema import RefResolver
from swagger_py_codegen.parser import RefNode

# TODO: datetime support


###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1/api'

definitions = {'definitions': {'VSModifyConflict': {'description': 'Requested virtual service already exist in the system.', 'properties': {'Error': {'enum': ['Requested virtual service already exist'], 'type': 'string'}}, 'type': 'object', 'required': ['Error']}, 'VirtualServiceModifyRequest': {'properties': {'name': {'pattern': '^[a-z0-9]{6}-[0-9]{2}\\.iphmx\\.com$', 'type': 'string', 'example': 'hc2516-81.iphmx.com'}, 'server_pool': {'properties': {'servers': {'items': {'$ref': '#/definitions/host'}, 'type': 'array'}, 'lb_algorithm': {'$ref': '#/definitions/LoadBalancer'}}, 'type': 'object', 'required': ['servers']}}, 'type': 'object'}, 'VSNotFoundErrorResponse': {'description': 'A response indicated the Virtual service does not exist.', 'properties': {'Error': {'enum': ['Virtual service with give id does not exist'], 'type': 'string'}}, 'type': 'object', 'required': ['Error']}, 'CreateVSNoFreeIP': {'description': 'There is no free IPs left in IPAM.', 'properties': {'Error': {'enum': ['There is no free IP in IPAM. Please contact IPAM adminstrator'], 'type': 'string'}}, 'type': 'object', 'required': ['Error']}, 'GeneralInternalErrorResponse': {'description': 'An error occurred whilst getting the site', 'properties': {'Error': {'enum': ['DataBase error occurred. Please contact owner team', 'Authentication error occurred.  Please contact owner team'], 'type': 'string'}}, 'type': 'object', 'required': ['Error']}, 'JWTAuthorizationErrorResponse': {'description': 'A Streamline IAM access token was not provided or it was invalid.', 'properties': {'Error': {'enum': ['Unauthorized'], 'type': 'string'}}, 'type': 'object', 'required': ['Error']}, 'LoadBalancer': {'enum': ['LB_ALGORITHM_LEAST_CONNECTIONS', 'LB_ALGORITHM_ROUND_ROBIN', 'LB_ALGORITHM_FASTEST_RESPONSE', 'LB_ALGORITHM_LEAST_LOAD'], 'type': 'string'}, 'Forbidden': {'properties': {'Error': {'enum': ['Forbidden'], 'type': 'string'}}, 'type': 'object', 'required': ['Error']}, 'nat': {'readOnly': True, 'properties': {'ip_address': {'$ref': '#/definitions/ip_address'}}, 'type': 'object'}, 'host': {'properties': {'ip': {'properties': {'addr': {'type': 'string', 'example': '10.8.128.53'}, 'type': {'type': 'string', 'example': 'V4'}}, 'type': 'object'}, 'enabled': {'type': 'boolean', 'example': True}}, 'type': 'object'}, 'CreateVSInvalidInputErrorResponse': {'description': 'One or more of the parameters required for this request were invalid, missing or unparseable.', 'properties': {'Error': {'enum': ['Provided site_id is invalid', 'Provided name is invalid', 'Provided loadbalancer algorithm is invalid or unsupported', 'Provided servers are invalid'], 'type': 'string'}}, 'type': 'object', 'required': ['Error']}, 'VirtualService': {'xml': {'name': 'VirtualService'}, 'properties': {'id': {'pattern': '^\\d{1,}-virtualservice-[a-z0-9_\\-]{36}$', 'readOnly': True, 'type': 'string', 'example': '2-virtualservice-a1074738-d032-44de-b663-45928b3db451'}, 'nat': {'$ref': '#/definitions/nat'}, 'name': {'pattern': '^[a-z0-9]{6}-[0-9]{2}\\.iphmx\\.com$', 'type': 'string', 'example': 'hc2516-81.iphmx.com'}, 'segment_id': {'format': 'int64', 'type': 'integer', 'example': '0'}, 'server_pool': {'properties': {'servers': {'items': {'$ref': '#/definitions/host'}, 'type': 'array'}, 'lb_algorithm': {'$ref': '#/definitions/LoadBalancer'}}, 'type': 'object', 'required': ['servers']}, 'deploymentStatus': {'description': 'Virtual Service deployment status', 'readOnly': True, 'type': 'string', 'enum': ['deploy_pending', 'deploy_in_progress', 'deploy_failed', 'deployed', 'delete_pending', 'delete_in_progress', 'delete_failed', 'deleted'], 'example': 'deleted'}, 'modifiedAt': {'readOnly': True, 'example': '2018-04-05T01:03:18.000Z', 'type': 'string', 'format': 'date-time'}, 'vip': {'$ref': '#/definitions/vip'}, 'site_id': {'format': 'int64', 'type': 'integer', 'example': '2'}, 'createdAt': {'readOnly': True, 'example': '2018-04-05T01:02:14.000Z', 'type': 'string', 'format': 'date-time'}}, 'type': 'object', 'required': ['site_id', 'segment_id', 'name', 'vip', 'server_pool']}, 'ip_address': {'properties': {'type': {'pattern': '^V(4|6)$', 'type': 'string', 'example': 'V4'}, 'address': {'pattern': '^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}$', 'type': 'string', 'example': '68.232.129.60'}}, 'type': 'object'}, 'VSModifyInvalidInput': {'description': 'One or more of the parameters required for this request were invalid, missing or unparseable.', 'properties': {'Error': {'enum': ['Provided site_id is invalid', 'Provided servers are invalid'], 'type': 'string'}}, 'type': 'object', 'required': ['Error']}, 'subnet': {'properties': {'subnet_id': {'pattern': '^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}$', 'type': 'string', 'example': '10.10.0.0'}, 'type': {'pattern': '^V(4|6)$', 'type': 'string', 'example': 'V4'}, 'mask_bits': {'type': 'integer', 'example': '24'}}, 'type': 'object'}, 'Segment': {'xml': {'name': 'Segment'}, 'properties': {'id': {'type': 'integer', 'format': 'int64'}, 'max_vs': {'type': 'integer', 'example': '250'}, 'subnets': {'items': {'$ref': '#/definitions/subnet'}, 'type': 'array'}, 'vlan': {'type': 'integer', 'example': '301'}, 'site_id': {'format': 'int64', 'type': 'integer', 'example': '2'}, 'avail_vs': {'type': 'integer', 'example': 200}}, 'type': 'object'}, 'SiteRequest': {'properties': {'provider': {'description': 'LB provider in the site', 'pattern': '(avi|not_avi)', 'type': 'string', 'example': 'avi'}, 'name': {'pattern': '^[a-z]{2,5}\\d{0,1}$', 'type': 'string', 'example': 'sv2'}}, 'type': 'object'}, 'InvalidSiteID': {'description': 'One or more of the parameters required for this request were invalid, missing or unparseable.', 'properties': {'Error': {'enum': ['Provided site_id is invalid'], 'type': 'string'}}, 'type': 'object', 'required': ['Error']}, 'VirtualServiceRequest': {'properties': {'nat': {'$ref': '#/definitions/nat'}, 'name': {'pattern': '^[a-z0-9]{6}-[0-9]{2}\\.iphmx\\.com$', 'type': 'string', 'example': 'hc2516-81.iphmx.com'}, 'segment_id': {'format': 'int64', 'type': 'integer', 'example': '0'}, 'server_pool': {'properties': {'servers': {'items': {'$ref': '#/definitions/host'}, 'type': 'array'}, 'lb_algorithm': {'$ref': '#/definitions/LoadBalancer'}}, 'type': 'object', 'required': ['servers']}, 'site_id': {'format': 'int64', 'type': 'integer', 'example': '2'}, 'vip': {'$ref': '#/definitions/vip'}}, 'type': 'object', 'required': ['site_id', 'segment_id', 'name', 'vip', 'server_pool']}, 'Site': {'xml': {'name': 'Site'}, 'properties': {'id': {'type': 'integer', 'format': 'int64'}, 'provider': {'description': 'LB provider in the site', 'type': 'string', 'example': 'avi'}, 'name': {'type': 'string', 'example': 'sv2'}, 'update_interval': {'description': 'Interval in seconds for each build of orchestrator', 'type': 'integer'}}, 'type': 'object'}, 'SiteNotFoundErrorResponse': {'description': 'A response indicated the provided site does not exist.', 'properties': {'Error': {'enum': ['Site not found'], 'type': 'string'}}, 'type': 'object', 'required': ['Error']}, 'vip': {'readOnly': True, 'properties': {'ip_address': {'$ref': '#/definitions/ip_address'}}, 'type': 'object'}}, 'parameters': {}}

validators = {
    ('sites_id', 'GET'): {'headers': {'properties': {'Authorization': {'description': 'A signed and valid Streamline IAM access token', 'type': 'string'}}, 'required': ['Authorization']}},
    ('virtualservice', 'GET'): {'headers': {'properties': {'Authorization': {'description': 'A signed and valid Streamline IAM access token', 'type': 'string'}}, 'required': ['Authorization']}, 'args': {'properties': {'Site': {'description': 'Filtering all sites by sites', 'required': False, 'type': 'string'}}, 'required': []}},
    ('virtualservice', 'POST'): {'json': {'$ref': '#/definitions/VirtualServiceRequest'}, 'headers': {'properties': {'Authorization': {'description': 'A signed and valid Streamline IAM access token', 'type': 'string'}}, 'required': ['Authorization']}},
    ('sites', 'POST'): {'json': {'$ref': '#/definitions/SiteRequest'}, 'headers': {'properties': {'Authorization': {'description': 'A signed and valid Streamline IAM access token', 'type': 'string'}}, 'required': ['Authorization']}},
    ('sites', 'GET'): {'headers': {'properties': {'Authorization': {'description': 'A signed and valid Streamline IAM access token', 'type': 'string'}}, 'required': ['Authorization']}},
    ('segment', 'GET'): {'headers': {'properties': {'Authorization': {'description': 'A signed and valid Streamline IAM access token', 'type': 'string'}}, 'required': ['Authorization']}, 'args': {'properties': {'site_id': {'description': 'filter based on site id, if site id isnt provided fetches all segments', 'type': 'string'}}, 'required': []}},
    ('virtualservice_id', 'PUT'): {'json': {'$ref': '#/definitions/VirtualServiceModifyRequest'}},
    ('virtualservice_id', 'GET'): {'args': {'properties': {'name': {'description': 'Customer name', 'type': 'string', 'required': False}, 'site_id': {'description': 'Site id for filter', 'type': 'string', 'required': False}}, 'required': []}},
    ('segment_getNextSegment', 'GET'): {'headers': {'properties': {'Authorization': {'description': 'A signed and valid Streamline IAM access token', 'type': 'string'}}, 'required': ['Authorization']}, 'args': {'properties': {'algorithm': {'description': 'Algorithm to use to get next segment. Options available are least virtual services in a segment or least loaded segment. Defaults to least_vs when this query isnt provided', 'items': {'enum': ['least_vs', 'least_loaded'], 'default': 'least_vs', 'type': 'string'}, 'type': 'array'}, 'site_id': {'description': 'filter based on site_id', 'type': 'string'}}, 'required': ['site_id']}},
}

filters = {
    ('sites_id', 'GET'): {200: {'schema': {'items': {'$ref': '#/definitions/Site'}, 'type': 'array'}, 'headers': None}, 401: {'schema': {'$ref': '#/definitions/JWTAuthorizationErrorResponse'}, 'headers': None}, 400: {'schema': {'$ref': '#/definitions/InvalidSiteID'}, 'headers': None}, 404: {'schema': {'$ref': '#/definitions/SiteNotFoundErrorResponse'}, 'headers': None}, 500: {'schema': {'$ref': '#/definitions/GeneralInternalErrorResponse'}, 'headers': None}},
    ('virtualservice', 'GET'): {200: {'schema': {'items': {'$ref': '#/definitions/VirtualService'}, 'type': 'array'}, 'headers': None}, 401: {'schema': {'$ref': '#/definitions/JWTAuthorizationErrorResponse'}, 'headers': None}, 400: {'schema': {'$ref': '#/definitions/InvalidSiteID'}, 'headers': None}, 404: {'schema': {'$ref': '#/definitions/VSNotFoundErrorResponse'}, 'headers': None}, 500: {'schema': {'$ref': '#/definitions/GeneralInternalErrorResponse'}, 'headers': None}},
    ('virtualservice', 'POST'): {400: {'schema': {'$ref': '#/definitions/CreateVSInvalidInputErrorResponse'}, 'headers': None}, 401: {'schema': {'$ref': '#/definitions/JWTAuthorizationErrorResponse'}, 'headers': None}, 403: {'schema': {'$ref': '#/definitions/Forbidden'}, 'headers': None}, 500: {'schema': {'$ref': '#/definitions/GeneralInternalErrorResponse'}, 'headers': None}, 503: {'schema': {'$ref': '#/definitions/CreateVSNoFreeIP'}, 'headers': None}, 409: {'schema': {'$ref': '#/definitions/VSModifyConflict'}, 'headers': None}, 202: {'schema': {'$ref': '#/definitions/VirtualService'}, 'headers': None}},
    ('sites', 'POST'): {400: {'schema': {'$ref': '#/definitions/InvalidSiteID'}, 'headers': None}, 201: {'schema': None, 'headers': None}, 500: {'schema': {'$ref': '#/definitions/GeneralInternalErrorResponse'}, 'headers': None}, 401: {'schema': {'$ref': '#/definitions/JWTAuthorizationErrorResponse'}, 'headers': None}},
    ('sites', 'GET'): {200: {'schema': {'items': {'$ref': '#/definitions/Site'}, 'type': 'array'}, 'headers': None}, 401: {'schema': {'$ref': '#/definitions/JWTAuthorizationErrorResponse'}, 'headers': None}, 500: {'schema': {'$ref': '#/definitions/GeneralInternalErrorResponse'}, 'headers': None}},
    ('segment', 'GET'): {200: {'schema': {'items': {'$ref': '#/definitions/Segment'}, 'type': 'array'}, 'headers': None}, 401: {'schema': {'$ref': '#/definitions/JWTAuthorizationErrorResponse'}, 'headers': None}, 500: {'schema': {'$ref': '#/definitions/GeneralInternalErrorResponse'}, 'headers': None}},
    ('virtualservice_id', 'DELETE'): {400: {'schema': {'$ref': '#/definitions/InvalidSiteID'}, 'headers': None}, 401: {'schema': {'$ref': '#/definitions/JWTAuthorizationErrorResponse'}, 'headers': None}, 403: {'schema': {'$ref': '#/definitions/Forbidden'}, 'headers': None}, 404: {'schema': {'$ref': '#/definitions/VSNotFoundErrorResponse'}, 'headers': None}, 500: {'schema': {'$ref': '#/definitions/GeneralInternalErrorResponse'}, 'headers': None}, 204: {'schema': None, 'headers': None}},
    ('virtualservice_id', 'PUT'): {400: {'schema': {'$ref': '#/definitions/VSModifyInvalidInput'}, 'headers': None}, 401: {'schema': {'$ref': '#/definitions/JWTAuthorizationErrorResponse'}, 'headers': None}, 403: {'schema': {'$ref': '#/definitions/Forbidden'}, 'headers': None}, 404: {'schema': {'$ref': '#/definitions/VSNotFoundErrorResponse'}, 'headers': None}, 409: {'schema': {'$ref': '#/definitions/VSModifyConflict'}, 'headers': None}, 202: {'schema': {'$ref': '#/definitions/VirtualService'}, 'headers': None}, 500: {'schema': {'$ref': '#/definitions/GeneralInternalErrorResponse'}, 'headers': None}},
    ('virtualservice_id', 'GET'): {400: {'schema': {'$ref': '#/definitions/InvalidSiteID'}, 'headers': None}, 401: {'schema': {'$ref': '#/definitions/JWTAuthorizationErrorResponse'}, 'headers': None}, 403: {'schema': {'$ref': '#/definitions/Forbidden'}, 'headers': None}, 404: {'schema': {'$ref': '#/definitions/VSNotFoundErrorResponse'}, 'headers': None}, 200: {'schema': {'$ref': '#/definitions/VirtualService'}, 'headers': None}, 500: {'schema': {'$ref': '#/definitions/GeneralInternalErrorResponse'}, 'headers': None}},
    ('segment_getNextSegment', 'GET'): {200: {'schema': {'items': {'$ref': '#/definitions/Segment'}, 'type': 'array'}, 'headers': None}, 401: {'schema': {'$ref': '#/definitions/JWTAuthorizationErrorResponse'}, 'headers': None}, 500: {'schema': {'$ref': '#/definitions/GeneralInternalErrorResponse'}, 'headers': None}},
}

scopes = {
    ('sites_id', 'GET'): [],
    ('virtualservice', 'GET'): [],
    ('virtualservice', 'POST'): [],
    ('sites', 'POST'): [],
    ('sites', 'GET'): [],
    ('segment', 'GET'): [],
    ('virtualservice_id', 'DELETE'): [],
    ('virtualservice_id', 'PUT'): [],
    ('virtualservice_id', 'GET'): [],
    ('segment_getNextSegment', 'GET'): [],
}

resolver = RefResolver.from_schema(definitions)

class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True, resolver=None):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults, resolver=resolver)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None, resolver=None):
    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key or '$ref' in _schema:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema is not False:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, (dict, RefNode)):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize_ref(schema, data):
        if resolver == None:
            raise TypeError("resolver must be provided")
        ref = schema.get(u"$ref")
        scope, resolved = resolver.resolve(ref)
        if resolved.get('nullable', False) and not data:
            return {}
        return _normalize(resolved, data)

    def _normalize(schema, data):
        if schema is True or schema == {}:
            return data
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
            'ref': _normalize_ref
        }
        type_ = schema.get('type', 'object')
        if type_ not in funcs:
            type_ = 'default'
        if schema.get(u'$ref', None):
            type_ = 'ref'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors
