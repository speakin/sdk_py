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


class Voiceprint1tonVerifyResponse(object):
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
        'union_id': 'str',
        'score': 'float'
    }

    attribute_map = {
        'union_id': 'unionID',
        'score': 'score'
    }

    def __init__(self, union_id=None, score=None):  # noqa: E501
        """Voiceprint1tonVerifyResponse - a model defined in OpenAPI"""  # noqa: E501

        self._union_id = None
        self._score = None
        self.discriminator = None

        if union_id is not None:
            self.union_id = union_id
        if score is not None:
            self.score = score

    @property
    def union_id(self):
        """Gets the union_id of this Voiceprint1tonVerifyResponse.  # noqa: E501

        union ID  # noqa: E501

        :return: The union_id of this Voiceprint1tonVerifyResponse.  # noqa: E501
        :rtype: str
        """
        return self._union_id

    @union_id.setter
    def union_id(self, union_id):
        """Sets the union_id of this Voiceprint1tonVerifyResponse.

        union ID  # noqa: E501

        :param union_id: The union_id of this Voiceprint1tonVerifyResponse.  # noqa: E501
        :type: str
        """

        self._union_id = union_id

    @property
    def score(self):
        """Gets the score of this Voiceprint1tonVerifyResponse.  # noqa: E501

        得分  # noqa: E501

        :return: The score of this Voiceprint1tonVerifyResponse.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Voiceprint1tonVerifyResponse.

        得分  # noqa: E501

        :param score: The score of this Voiceprint1tonVerifyResponse.  # noqa: E501
        :type: float
        """

        self._score = score

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
        if not isinstance(other, Voiceprint1tonVerifyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
