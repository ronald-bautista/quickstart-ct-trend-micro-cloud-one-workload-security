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

from deepsecurity.models.custom_attribute import CustomAttribute  # noqa: F401,E501


class ESXSummary(object):
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
        'manufacturer': 'str',
        'model': 'str',
        'processors': 'str',
        'processor_type': 'str',
        'number_of_nics': 'str',
        'state': 'str',
        'virtual_machines': 'str',
        'v_motion_enabled': 'str',
        'custom_attributes': 'list[CustomAttribute]',
        'tpm_enabled': 'bool',
        'tpm_alerts_enabled': 'bool',
        'tpm_has_data': 'bool',
        'tpm_last_checked': 'int'
    }

    attribute_map = {
        'manufacturer': 'manufacturer',
        'model': 'model',
        'processors': 'processors',
        'processor_type': 'processorType',
        'number_of_nics': 'numberOfNICs',
        'state': 'state',
        'virtual_machines': 'virtualMachines',
        'v_motion_enabled': 'vMotionEnabled',
        'custom_attributes': 'customAttributes',
        'tpm_enabled': 'TPMEnabled',
        'tpm_alerts_enabled': 'TPMAlertsEnabled',
        'tpm_has_data': 'TPMHasData',
        'tpm_last_checked': 'TPMLastChecked'
    }

    def __init__(self, manufacturer=None, model=None, processors=None, processor_type=None, number_of_nics=None, state=None, virtual_machines=None, v_motion_enabled=None, custom_attributes=None, tpm_enabled=None, tpm_alerts_enabled=None, tpm_has_data=None, tpm_last_checked=None):  # noqa: E501
        """ESXSummary - a model defined in Swagger"""  # noqa: E501

        self._manufacturer = None
        self._model = None
        self._processors = None
        self._processor_type = None
        self._number_of_nics = None
        self._state = None
        self._virtual_machines = None
        self._v_motion_enabled = None
        self._custom_attributes = None
        self._tpm_enabled = None
        self._tpm_alerts_enabled = None
        self._tpm_has_data = None
        self._tpm_last_checked = None
        self.discriminator = None

        if manufacturer is not None:
            self.manufacturer = manufacturer
        if model is not None:
            self.model = model
        if processors is not None:
            self.processors = processors
        if processor_type is not None:
            self.processor_type = processor_type
        if number_of_nics is not None:
            self.number_of_nics = number_of_nics
        if state is not None:
            self.state = state
        if virtual_machines is not None:
            self.virtual_machines = virtual_machines
        if v_motion_enabled is not None:
            self.v_motion_enabled = v_motion_enabled
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes
        if tpm_enabled is not None:
            self.tpm_enabled = tpm_enabled
        if tpm_alerts_enabled is not None:
            self.tpm_alerts_enabled = tpm_alerts_enabled
        if tpm_has_data is not None:
            self.tpm_has_data = tpm_has_data
        if tpm_last_checked is not None:
            self.tpm_last_checked = tpm_last_checked

    @property
    def manufacturer(self):
        """Gets the manufacturer of this ESXSummary.  # noqa: E501

        Manufacturer of the ESX. Searchable as String.  # noqa: E501

        :return: The manufacturer of this ESXSummary.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this ESXSummary.

        Manufacturer of the ESX. Searchable as String.  # noqa: E501

        :param manufacturer: The manufacturer of this ESXSummary.  # noqa: E501
        :type: str
        """

        self._manufacturer = manufacturer

    @property
    def model(self):
        """Gets the model of this ESXSummary.  # noqa: E501

        Model of the ESX. Searchable as String.  # noqa: E501

        :return: The model of this ESXSummary.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ESXSummary.

        Model of the ESX. Searchable as String.  # noqa: E501

        :param model: The model of this ESXSummary.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def processors(self):
        """Gets the processors of this ESXSummary.  # noqa: E501

        Quantity and processor speed of the ESX's processors. Searchable as Numeric.  # noqa: E501

        :return: The processors of this ESXSummary.  # noqa: E501
        :rtype: str
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        """Sets the processors of this ESXSummary.

        Quantity and processor speed of the ESX's processors. Searchable as Numeric.  # noqa: E501

        :param processors: The processors of this ESXSummary.  # noqa: E501
        :type: str
        """

        self._processors = processors

    @property
    def processor_type(self):
        """Gets the processor_type of this ESXSummary.  # noqa: E501

        Detailed information on the make and model of the ESX's processor. Searchable as String.  # noqa: E501

        :return: The processor_type of this ESXSummary.  # noqa: E501
        :rtype: str
        """
        return self._processor_type

    @processor_type.setter
    def processor_type(self, processor_type):
        """Sets the processor_type of this ESXSummary.

        Detailed information on the make and model of the ESX's processor. Searchable as String.  # noqa: E501

        :param processor_type: The processor_type of this ESXSummary.  # noqa: E501
        :type: str
        """

        self._processor_type = processor_type

    @property
    def number_of_nics(self):
        """Gets the number_of_nics of this ESXSummary.  # noqa: E501

        Number of Network interface controllers the ESX has. Searchable as Numeric.  # noqa: E501

        :return: The number_of_nics of this ESXSummary.  # noqa: E501
        :rtype: str
        """
        return self._number_of_nics

    @number_of_nics.setter
    def number_of_nics(self, number_of_nics):
        """Sets the number_of_nics of this ESXSummary.

        Number of Network interface controllers the ESX has. Searchable as Numeric.  # noqa: E501

        :param number_of_nics: The number_of_nics of this ESXSummary.  # noqa: E501
        :type: str
        """

        self._number_of_nics = number_of_nics

    @property
    def state(self):
        """Gets the state of this ESXSummary.  # noqa: E501

        State of the ESX.  # noqa: E501

        :return: The state of this ESXSummary.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ESXSummary.

        State of the ESX.  # noqa: E501

        :param state: The state of this ESXSummary.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def virtual_machines(self):
        """Gets the virtual_machines of this ESXSummary.  # noqa: E501

        Number of virtual machines hosted on the ESX.  # noqa: E501

        :return: The virtual_machines of this ESXSummary.  # noqa: E501
        :rtype: str
        """
        return self._virtual_machines

    @virtual_machines.setter
    def virtual_machines(self, virtual_machines):
        """Sets the virtual_machines of this ESXSummary.

        Number of virtual machines hosted on the ESX.  # noqa: E501

        :param virtual_machines: The virtual_machines of this ESXSummary.  # noqa: E501
        :type: str
        """

        self._virtual_machines = virtual_machines

    @property
    def v_motion_enabled(self):
        """Gets the v_motion_enabled of this ESXSummary.  # noqa: E501

        Indicates whether vMotion is enabled on the ESX. The is value is true if enabled. Searchable as Boolean.  # noqa: E501

        :return: The v_motion_enabled of this ESXSummary.  # noqa: E501
        :rtype: str
        """
        return self._v_motion_enabled

    @v_motion_enabled.setter
    def v_motion_enabled(self, v_motion_enabled):
        """Sets the v_motion_enabled of this ESXSummary.

        Indicates whether vMotion is enabled on the ESX. The is value is true if enabled. Searchable as Boolean.  # noqa: E501

        :param v_motion_enabled: The v_motion_enabled of this ESXSummary.  # noqa: E501
        :type: str
        """

        self._v_motion_enabled = v_motion_enabled

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this ESXSummary.  # noqa: E501

        List of name/value pairs of ESX Custom Attributes  # noqa: E501

        :return: The custom_attributes of this ESXSummary.  # noqa: E501
        :rtype: list[CustomAttribute]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this ESXSummary.

        List of name/value pairs of ESX Custom Attributes  # noqa: E501

        :param custom_attributes: The custom_attributes of this ESXSummary.  # noqa: E501
        :type: list[CustomAttribute]
        """

        self._custom_attributes = custom_attributes

    @property
    def tpm_enabled(self):
        """Gets the tpm_enabled of this ESXSummary.  # noqa: E501


        :return: The tpm_enabled of this ESXSummary.  # noqa: E501
        :rtype: bool
        """
        return self._tpm_enabled

    @tpm_enabled.setter
    def tpm_enabled(self, tpm_enabled):
        """Sets the tpm_enabled of this ESXSummary.


        :param tpm_enabled: The tpm_enabled of this ESXSummary.  # noqa: E501
        :type: bool
        """

        self._tpm_enabled = tpm_enabled

    @property
    def tpm_alerts_enabled(self):
        """Gets the tpm_alerts_enabled of this ESXSummary.  # noqa: E501


        :return: The tpm_alerts_enabled of this ESXSummary.  # noqa: E501
        :rtype: bool
        """
        return self._tpm_alerts_enabled

    @tpm_alerts_enabled.setter
    def tpm_alerts_enabled(self, tpm_alerts_enabled):
        """Sets the tpm_alerts_enabled of this ESXSummary.


        :param tpm_alerts_enabled: The tpm_alerts_enabled of this ESXSummary.  # noqa: E501
        :type: bool
        """

        self._tpm_alerts_enabled = tpm_alerts_enabled

    @property
    def tpm_has_data(self):
        """Gets the tpm_has_data of this ESXSummary.  # noqa: E501


        :return: The tpm_has_data of this ESXSummary.  # noqa: E501
        :rtype: bool
        """
        return self._tpm_has_data

    @tpm_has_data.setter
    def tpm_has_data(self, tpm_has_data):
        """Sets the tpm_has_data of this ESXSummary.


        :param tpm_has_data: The tpm_has_data of this ESXSummary.  # noqa: E501
        :type: bool
        """

        self._tpm_has_data = tpm_has_data

    @property
    def tpm_last_checked(self):
        """Gets the tpm_last_checked of this ESXSummary.  # noqa: E501


        :return: The tpm_last_checked of this ESXSummary.  # noqa: E501
        :rtype: int
        """
        return self._tpm_last_checked

    @tpm_last_checked.setter
    def tpm_last_checked(self, tpm_last_checked):
        """Sets the tpm_last_checked of this ESXSummary.


        :param tpm_last_checked: The tpm_last_checked of this ESXSummary.  # noqa: E501
        :type: int
        """

        self._tpm_last_checked = tpm_last_checked

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
        if issubclass(ESXSummary, dict):
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
        if not isinstance(other, ESXSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

