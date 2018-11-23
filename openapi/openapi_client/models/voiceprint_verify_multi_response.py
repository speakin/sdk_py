# coding: utf-8

"""
    声纹云api

    api document  # noqa: E501

    OpenAPI spec version: /cloudapi/v1beta
    Contact: xiachengjia@speakin.mobi
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class VoiceprintVerifyMultiResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'report': 'list[VoiceprintVerifyMultiReport]'
    }

    attribute_map = {
        'report': 'report'
    }

    def __init__(self, report=None):  # noqa: E501
        """VoiceprintVerifyMultiResponse - a model defined in OpenAPI"""  # noqa: E501

        self._report = None
        self.discriminator = None

        if report is not None:
            self.report = report

    @property
    def report(self):
        """Gets the report of this VoiceprintVerifyMultiResponse.  # noqa: E501

        结果  # noqa: E501

        :return: The report of this VoiceprintVerifyMultiResponse.  # noqa: E501
        :rtype: list[VoiceprintVerifyMultiReport]
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this VoiceprintVerifyMultiResponse.

        结果  # noqa: E501

        :param report: The report of this VoiceprintVerifyMultiResponse.  # noqa: E501
        :type: list[VoiceprintVerifyMultiReport]
        """

        self._report = report

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VoiceprintVerifyMultiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other