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

from deepsecurity.models.software_change_review_result import SoftwareChangeReviewResult  # noqa: F401,E501


class SoftwareChangeReview(object):
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
        'software_change_ids': 'list[int]',
        'action': 'str',
        'software_change_review_results': 'list[SoftwareChangeReviewResult]'
    }

    attribute_map = {
        'software_change_ids': 'softwareChangeIDs',
        'action': 'action',
        'software_change_review_results': 'softwareChangeReviewResults'
    }

    def __init__(self, software_change_ids=None, action=None, software_change_review_results=None):  # noqa: E501
        """SoftwareChangeReview - a model defined in Swagger"""  # noqa: E501

        self._software_change_ids = None
        self._action = None
        self._software_change_review_results = None
        self.discriminator = None

        if software_change_ids is not None:
            self.software_change_ids = software_change_ids
        if action is not None:
            self.action = action
        if software_change_review_results is not None:
            self.software_change_review_results = software_change_review_results

    @property
    def software_change_ids(self):
        """Gets the software_change_ids of this SoftwareChangeReview.  # noqa: E501

        List of software change IDs.  # noqa: E501

        :return: The software_change_ids of this SoftwareChangeReview.  # noqa: E501
        :rtype: list[int]
        """
        return self._software_change_ids

    @software_change_ids.setter
    def software_change_ids(self, software_change_ids):
        """Sets the software_change_ids of this SoftwareChangeReview.

        List of software change IDs.  # noqa: E501

        :param software_change_ids: The software_change_ids of this SoftwareChangeReview.  # noqa: E501
        :type: list[int]
        """

        self._software_change_ids = software_change_ids

    @property
    def action(self):
        """Gets the action of this SoftwareChangeReview.  # noqa: E501

        Action to perform on the software changes.  # noqa: E501

        :return: The action of this SoftwareChangeReview.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this SoftwareChangeReview.

        Action to perform on the software changes.  # noqa: E501

        :param action: The action of this SoftwareChangeReview.  # noqa: E501
        :type: str
        """
        allowed_values = ["allow", "block"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def software_change_review_results(self):
        """Gets the software_change_review_results of this SoftwareChangeReview.  # noqa: E501

        Results of software changes.  # noqa: E501

        :return: The software_change_review_results of this SoftwareChangeReview.  # noqa: E501
        :rtype: list[SoftwareChangeReviewResult]
        """
        return self._software_change_review_results

    @software_change_review_results.setter
    def software_change_review_results(self, software_change_review_results):
        """Sets the software_change_review_results of this SoftwareChangeReview.

        Results of software changes.  # noqa: E501

        :param software_change_review_results: The software_change_review_results of this SoftwareChangeReview.  # noqa: E501
        :type: list[SoftwareChangeReviewResult]
        """

        self._software_change_review_results = software_change_review_results

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
        if issubclass(SoftwareChangeReview, dict):
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
        if not isinstance(other, SoftwareChangeReview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

