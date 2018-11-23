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


class VoiceprintCtcdasrResponse(object):
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
        'asr_string': 'str'
    }

    attribute_map = {
        'asr_string': 'asrString'
    }

    def __init__(self, asr_string=None):  # noqa: E501
        """VoiceprintCtcdasrResponse - a model defined in OpenAPI"""  # noqa: E501

        self._asr_string = None
        self.discriminator = None

        if asr_string is not None:
            self.asr_string = asr_string

    @property
    def asr_string(self):
        """Gets the asr_string of this VoiceprintCtcdasrResponse.  # noqa: E501

        数字asr  # noqa: E501

        :return: The asr_string of this VoiceprintCtcdasrResponse.  # noqa: E501
        :rtype: str
        """
        return self._asr_string

    @asr_string.setter
    def asr_string(self, asr_string):
        """Sets the asr_string of this VoiceprintCtcdasrResponse.

        数字asr  # noqa: E501

        :param asr_string: The asr_string of this VoiceprintCtcdasrResponse.  # noqa: E501
        :type: str
        """

        self._asr_string = asr_string

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
        if not isinstance(other, VoiceprintCtcdasrResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other