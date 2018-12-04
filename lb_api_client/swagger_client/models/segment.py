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

from swagger_client.models.subnet import Subnet  # noqa: F401,E501


class Segment(object):
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
        'id': 'int',
        'site_id': 'int',
        'max_vs': 'int',
        'avail_vs': 'int',
        'vlan': 'int',
        'subnets': 'list[Subnet]'
    }

    attribute_map = {
        'id': 'id',
        'site_id': 'site_id',
        'max_vs': 'max_vs',
        'avail_vs': 'avail_vs',
        'vlan': 'vlan',
        'subnets': 'subnets'
    }

    def __init__(self, id=None, site_id=None, max_vs=None, avail_vs=None, vlan=None, subnets=None):  # noqa: E501
        """Segment - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._site_id = None
        self._max_vs = None
        self._avail_vs = None
        self._vlan = None
        self._subnets = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if site_id is not None:
            self.site_id = site_id
        if max_vs is not None:
            self.max_vs = max_vs
        if avail_vs is not None:
            self.avail_vs = avail_vs
        if vlan is not None:
            self.vlan = vlan
        if subnets is not None:
            self.subnets = subnets

    @property
    def id(self):
        """Gets the id of this Segment.  # noqa: E501


        :return: The id of this Segment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Segment.


        :param id: The id of this Segment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def site_id(self):
        """Gets the site_id of this Segment.  # noqa: E501


        :return: The site_id of this Segment.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Segment.


        :param site_id: The site_id of this Segment.  # noqa: E501
        :type: int
        """

        self._site_id = site_id

    @property
    def max_vs(self):
        """Gets the max_vs of this Segment.  # noqa: E501


        :return: The max_vs of this Segment.  # noqa: E501
        :rtype: int
        """
        return self._max_vs

    @max_vs.setter
    def max_vs(self, max_vs):
        """Sets the max_vs of this Segment.


        :param max_vs: The max_vs of this Segment.  # noqa: E501
        :type: int
        """

        self._max_vs = max_vs

    @property
    def avail_vs(self):
        """Gets the avail_vs of this Segment.  # noqa: E501


        :return: The avail_vs of this Segment.  # noqa: E501
        :rtype: int
        """
        return self._avail_vs

    @avail_vs.setter
    def avail_vs(self, avail_vs):
        """Sets the avail_vs of this Segment.


        :param avail_vs: The avail_vs of this Segment.  # noqa: E501
        :type: int
        """

        self._avail_vs = avail_vs

    @property
    def vlan(self):
        """Gets the vlan of this Segment.  # noqa: E501


        :return: The vlan of this Segment.  # noqa: E501
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this Segment.


        :param vlan: The vlan of this Segment.  # noqa: E501
        :type: int
        """

        self._vlan = vlan

    @property
    def subnets(self):
        """Gets the subnets of this Segment.  # noqa: E501


        :return: The subnets of this Segment.  # noqa: E501
        :rtype: list[Subnet]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        """Sets the subnets of this Segment.


        :param subnets: The subnets of this Segment.  # noqa: E501
        :type: list[Subnet]
        """

        self._subnets = subnets

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
        if issubclass(Segment, dict):
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
        if not isinstance(other, Segment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
