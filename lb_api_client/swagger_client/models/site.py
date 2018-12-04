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


class Site(object):
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
        'name': 'str',
        'provider': 'str',
        'update_interval': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'provider': 'provider',
        'update_interval': 'update_interval'
    }

    def __init__(self, id=None, name=None, provider=None, update_interval=None):  # noqa: E501
        """Site - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._provider = None
        self._update_interval = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if provider is not None:
            self.provider = provider
        if update_interval is not None:
            self.update_interval = update_interval

    @property
    def id(self):
        """Gets the id of this Site.  # noqa: E501


        :return: The id of this Site.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Site.


        :param id: The id of this Site.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Site.  # noqa: E501


        :return: The name of this Site.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Site.


        :param name: The name of this Site.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this Site.  # noqa: E501

        LB provider in the site  # noqa: E501

        :return: The provider of this Site.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this Site.

        LB provider in the site  # noqa: E501

        :param provider: The provider of this Site.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def update_interval(self):
        """Gets the update_interval of this Site.  # noqa: E501

        Interval in seconds for each build of orchestrator  # noqa: E501

        :return: The update_interval of this Site.  # noqa: E501
        :rtype: int
        """
        return self._update_interval

    @update_interval.setter
    def update_interval(self, update_interval):
        """Sets the update_interval of this Site.

        Interval in seconds for each build of orchestrator  # noqa: E501

        :param update_interval: The update_interval of this Site.  # noqa: E501
        :type: int
        """

        self._update_interval = update_interval

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
        if issubclass(Site, dict):
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
        if not isinstance(other, Site):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other