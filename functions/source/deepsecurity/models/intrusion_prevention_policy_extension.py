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

from deepsecurity.models.policy_module_status import PolicyModuleStatus  # noqa: F401,E501


class IntrusionPreventionPolicyExtension(object):
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
        'state': 'str',
        'module_status': 'PolicyModuleStatus',
        'rule_ids': 'list[int]',
        'application_type_ids': 'list[int]'
    }

    attribute_map = {
        'state': 'state',
        'module_status': 'moduleStatus',
        'rule_ids': 'ruleIDs',
        'application_type_ids': 'applicationTypeIDs'
    }

    def __init__(self, state=None, module_status=None, rule_ids=None, application_type_ids=None):  # noqa: E501
        """IntrusionPreventionPolicyExtension - a model defined in Swagger"""  # noqa: E501

        self._state = None
        self._module_status = None
        self._rule_ids = None
        self._application_type_ids = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if module_status is not None:
            self.module_status = module_status
        if rule_ids is not None:
            self.rule_ids = rule_ids
        if application_type_ids is not None:
            self.application_type_ids = application_type_ids

    @property
    def state(self):
        """Gets the state of this IntrusionPreventionPolicyExtension.  # noqa: E501

        Module state.  # noqa: E501

        :return: The state of this IntrusionPreventionPolicyExtension.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this IntrusionPreventionPolicyExtension.

        Module state.  # noqa: E501

        :param state: The state of this IntrusionPreventionPolicyExtension.  # noqa: E501
        :type: str
        """
        allowed_values = ["inherited", "prevent", "detect", "off"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def module_status(self):
        """Gets the module_status of this IntrusionPreventionPolicyExtension.  # noqa: E501


        :return: The module_status of this IntrusionPreventionPolicyExtension.  # noqa: E501
        :rtype: PolicyModuleStatus
        """
        return self._module_status

    @module_status.setter
    def module_status(self, module_status):
        """Sets the module_status of this IntrusionPreventionPolicyExtension.


        :param module_status: The module_status of this IntrusionPreventionPolicyExtension.  # noqa: E501
        :type: PolicyModuleStatus
        """

        self._module_status = module_status

    @property
    def rule_ids(self):
        """Gets the rule_ids of this IntrusionPreventionPolicyExtension.  # noqa: E501

        IDs of the assigned Intrusion Prevention rules.  # noqa: E501

        :return: The rule_ids of this IntrusionPreventionPolicyExtension.  # noqa: E501
        :rtype: list[int]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        """Sets the rule_ids of this IntrusionPreventionPolicyExtension.

        IDs of the assigned Intrusion Prevention rules.  # noqa: E501

        :param rule_ids: The rule_ids of this IntrusionPreventionPolicyExtension.  # noqa: E501
        :type: list[int]
        """

        self._rule_ids = rule_ids

    @property
    def application_type_ids(self):
        """Gets the application_type_ids of this IntrusionPreventionPolicyExtension.  # noqa: E501

        IDs of the assigned Application Types.  # noqa: E501

        :return: The application_type_ids of this IntrusionPreventionPolicyExtension.  # noqa: E501
        :rtype: list[int]
        """
        return self._application_type_ids

    @application_type_ids.setter
    def application_type_ids(self, application_type_ids):
        """Sets the application_type_ids of this IntrusionPreventionPolicyExtension.

        IDs of the assigned Application Types.  # noqa: E501

        :param application_type_ids: The application_type_ids of this IntrusionPreventionPolicyExtension.  # noqa: E501
        :type: list[int]
        """

        self._application_type_ids = application_type_ids

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
        if issubclass(IntrusionPreventionPolicyExtension, dict):
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
        if not isinstance(other, IntrusionPreventionPolicyExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

