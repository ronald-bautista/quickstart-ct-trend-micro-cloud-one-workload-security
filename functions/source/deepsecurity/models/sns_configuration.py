# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 12.5.841
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SnsConfiguration(object):
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
        'access_key': 'str',
        'secret_key': 'str',
        'topic_arn': 'str',
        'advanced_configuration': 'str',
        'forwarding_enabled': 'bool'
    }

    attribute_map = {
        'access_key': 'accessKey',
        'secret_key': 'secretKey',
        'topic_arn': 'topicARN',
        'advanced_configuration': 'advancedConfiguration',
        'forwarding_enabled': 'forwardingEnabled'
    }

    def __init__(self, access_key=None, secret_key=None, topic_arn=None, advanced_configuration=None, forwarding_enabled=None):  # noqa: E501
        """SnsConfiguration - a model defined in Swagger"""  # noqa: E501

        self._access_key = None
        self._secret_key = None
        self._topic_arn = None
        self._advanced_configuration = None
        self._forwarding_enabled = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if topic_arn is not None:
            self.topic_arn = topic_arn
        if advanced_configuration is not None:
            self.advanced_configuration = advanced_configuration
        if forwarding_enabled is not None:
            self.forwarding_enabled = forwarding_enabled

    @property
    def access_key(self):
        """Gets the access_key of this SnsConfiguration.  # noqa: E501

        AWS access key that has permissions to write to the SNS topic.  # noqa: E501

        :return: The access_key of this SnsConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this SnsConfiguration.

        AWS access key that has permissions to write to the SNS topic.  # noqa: E501

        :param access_key: The access_key of this SnsConfiguration.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def secret_key(self):
        """Gets the secret_key of this SnsConfiguration.  # noqa: E501

        AWS secret key.  # noqa: E501

        :return: The secret_key of this SnsConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this SnsConfiguration.

        AWS secret key.  # noqa: E501

        :param secret_key: The secret_key of this SnsConfiguration.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def topic_arn(self):
        """Gets the topic_arn of this SnsConfiguration.  # noqa: E501

        SNS topic to forward to. This should be provided by the customer/tenant.  # noqa: E501

        :return: The topic_arn of this SnsConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._topic_arn

    @topic_arn.setter
    def topic_arn(self, topic_arn):
        """Sets the topic_arn of this SnsConfiguration.

        SNS topic to forward to. This should be provided by the customer/tenant.  # noqa: E501

        :param topic_arn: The topic_arn of this SnsConfiguration.  # noqa: E501
        :type: str
        """

        self._topic_arn = topic_arn

    @property
    def advanced_configuration(self):
        """Gets the advanced_configuration of this SnsConfiguration.  # noqa: E501

        JSON Configuration specifying customized forwarding rules.  # noqa: E501

        :return: The advanced_configuration of this SnsConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._advanced_configuration

    @advanced_configuration.setter
    def advanced_configuration(self, advanced_configuration):
        """Sets the advanced_configuration of this SnsConfiguration.

        JSON Configuration specifying customized forwarding rules.  # noqa: E501

        :param advanced_configuration: The advanced_configuration of this SnsConfiguration.  # noqa: E501
        :type: str
        """

        self._advanced_configuration = advanced_configuration

    @property
    def forwarding_enabled(self):
        """Gets the forwarding_enabled of this SnsConfiguration.  # noqa: E501

        Is SNS forwarding enabled for this tenant.  # noqa: E501

        :return: The forwarding_enabled of this SnsConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._forwarding_enabled

    @forwarding_enabled.setter
    def forwarding_enabled(self, forwarding_enabled):
        """Sets the forwarding_enabled of this SnsConfiguration.

        Is SNS forwarding enabled for this tenant.  # noqa: E501

        :param forwarding_enabled: The forwarding_enabled of this SnsConfiguration.  # noqa: E501
        :type: bool
        """

        self._forwarding_enabled = forwarding_enabled

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
        if issubclass(SnsConfiguration, dict):
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
        if not isinstance(other, SnsConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

