# coding: utf-8

"""
    CESv2 Remail Network API

    CESv2 Remail Network API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: cie-eng.network-hps-team@cisco.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.nat import Nat  # noqa: F401,E501
from swagger_client.models.vip import Vip  # noqa: F401,E501
from swagger_client.models.virtual_service_server_pool import VirtualServiceServerPool  # noqa: F401,E501


class VirtualService(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'site_id': 'int',
        'segment_id': 'int',
        'name': 'str',
        'vip': 'Vip',
        'nat': 'Nat',
        'server_pool': 'VirtualServiceServerPool',
        'created_at': 'datetime',
        'modified_at': 'datetime',
        'deployment_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'site_id': 'site_id',
        'segment_id': 'segment_id',
        'name': 'name',
        'vip': 'vip',
        'nat': 'nat',
        'server_pool': 'server_pool',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt',
        'deployment_status': 'deploymentStatus'
    }

    def __init__(self, id=None, site_id=None, segment_id=None, name=None, vip=None, nat=None, server_pool=None, created_at=None, modified_at=None, deployment_status=None):  # noqa: E501
        """VirtualService - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._site_id = None
        self._segment_id = None
        self._name = None
        self._vip = None
        self._nat = None
        self._server_pool = None
        self._created_at = None
        self._modified_at = None
        self._deployment_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if site_id is not None:
            self.site_id = site_id
        if segment_id is not None:
            self.segment_id = segment_id
        if name is not None:
            self.name = name
        if vip is not None:
            self.vip = vip
        if nat is not None:
            self.nat = nat
        if server_pool is not None:
            self.server_pool = server_pool
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if deployment_status is not None:
            self.deployment_status = deployment_status

    @property
    def id(self):
        """Gets the id of this VirtualService.  # noqa: E501


        :return: The id of this VirtualService.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualService.


        :param id: The id of this VirtualService.  # noqa: E501
        :type: str
        """
        if id is not None and not re.search(r'^\\d{1,}-virtualservice-[a-z0-9_\\-]{36}$', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/^\\d{1,}-virtualservice-[a-z0-9_\\-]{36}$/`")  # noqa: E501

        self._id = id

    @property
    def site_id(self):
        """Gets the site_id of this VirtualService.  # noqa: E501


        :return: The site_id of this VirtualService.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this VirtualService.


        :param site_id: The site_id of this VirtualService.  # noqa: E501
        :type: int
        """

        self._site_id = site_id

    @property
    def segment_id(self):
        """Gets the segment_id of this VirtualService.  # noqa: E501


        :return: The segment_id of this VirtualService.  # noqa: E501
        :rtype: int
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """Sets the segment_id of this VirtualService.


        :param segment_id: The segment_id of this VirtualService.  # noqa: E501
        :type: int
        """

        self._segment_id = segment_id

    @property
    def name(self):
        """Gets the name of this VirtualService.  # noqa: E501


        :return: The name of this VirtualService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualService.


        :param name: The name of this VirtualService.  # noqa: E501
        :type: str
        """
        if name is not None and not re.search(r'^[a-z0-9]{6}-[0-9]{2}\\.iphmx\\.com$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-z0-9]{6}-[0-9]{2}\\.iphmx\\.com$/`")  # noqa: E501

        self._name = name

    @property
    def vip(self):
        """Gets the vip of this VirtualService.  # noqa: E501


        :return: The vip of this VirtualService.  # noqa: E501
        :rtype: Vip
        """
        return self._vip

    @vip.setter
    def vip(self, vip):
        """Sets the vip of this VirtualService.


        :param vip: The vip of this VirtualService.  # noqa: E501
        :type: Vip
        """

        self._vip = vip

    @property
    def nat(self):
        """Gets the nat of this VirtualService.  # noqa: E501


        :return: The nat of this VirtualService.  # noqa: E501
        :rtype: Nat
        """
        return self._nat

    @nat.setter
    def nat(self, nat):
        """Sets the nat of this VirtualService.


        :param nat: The nat of this VirtualService.  # noqa: E501
        :type: Nat
        """

        self._nat = nat

    @property
    def server_pool(self):
        """Gets the server_pool of this VirtualService.  # noqa: E501


        :return: The server_pool of this VirtualService.  # noqa: E501
        :rtype: VirtualServiceServerPool
        """
        return self._server_pool

    @server_pool.setter
    def server_pool(self, server_pool):
        """Sets the server_pool of this VirtualService.


        :param server_pool: The server_pool of this VirtualService.  # noqa: E501
        :type: VirtualServiceServerPool
        """

        self._server_pool = server_pool

    @property
    def created_at(self):
        """Gets the created_at of this VirtualService.  # noqa: E501


        :return: The created_at of this VirtualService.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VirtualService.


        :param created_at: The created_at of this VirtualService.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this VirtualService.  # noqa: E501


        :return: The modified_at of this VirtualService.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this VirtualService.


        :param modified_at: The modified_at of this VirtualService.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def deployment_status(self):
        """Gets the deployment_status of this VirtualService.  # noqa: E501

        Virtual Service deployment status  # noqa: E501

        :return: The deployment_status of this VirtualService.  # noqa: E501
        :rtype: str
        """
        return self._deployment_status

    @deployment_status.setter
    def deployment_status(self, deployment_status):
        """Sets the deployment_status of this VirtualService.

        Virtual Service deployment status  # noqa: E501

        :param deployment_status: The deployment_status of this VirtualService.  # noqa: E501
        :type: str
        """
        allowed_values = ["deploy_pending", "deploy_in_progress", "deploy_failed", "deployed", "delete_pending", "delete_in_progress", "delete_failed", "deleted"]  # noqa: E501
        if deployment_status not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_status` ({0}), must be one of {1}"  # noqa: E501
                .format(deployment_status, allowed_values)
            )

        self._deployment_status = deployment_status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(VirtualService, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VirtualService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
