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


class VoiceprinttopnVerifyRequest(object):
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
        'app_name': 'str',
        'url': 'str',
        'sampling_rate': 'str',
        'topn': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'app_name': 'appName',
        'url': 'url',
        'sampling_rate': 'samplingRate',
        'topn': 'topn',
        'timestamp': 'timestamp'
    }

    def __init__(self, app_name=None, url=None, sampling_rate=None, topn=None, timestamp=None):  # noqa: E501
        """VoiceprinttopnVerifyRequest - a model defined in OpenAPI"""  # noqa: E501

        self._app_name = None
        self._url = None
        self._sampling_rate = None
        self._topn = None
        self._timestamp = None
        self.discriminator = None

        self.app_name = app_name
        self.url = url
        self.sampling_rate = sampling_rate
        self.topn = topn
        self.timestamp = timestamp

    @property
    def app_name(self):
        """Gets the app_name of this VoiceprinttopnVerifyRequest.  # noqa: E501


        :return: The app_name of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this VoiceprinttopnVerifyRequest.


        :param app_name: The app_name of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :type: str
        """
        if app_name is None:
            raise ValueError("Invalid value for `app_name`, must not be `None`")  # noqa: E501

        self._app_name = app_name

    @property
    def url(self):
        """Gets the url of this VoiceprinttopnVerifyRequest.  # noqa: E501


        :return: The url of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this VoiceprinttopnVerifyRequest.


        :param url: The url of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def sampling_rate(self):
        """Gets the sampling_rate of this VoiceprinttopnVerifyRequest.  # noqa: E501


        :return: The sampling_rate of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :rtype: str
        """
        return self._sampling_rate

    @sampling_rate.setter
    def sampling_rate(self, sampling_rate):
        """Sets the sampling_rate of this VoiceprinttopnVerifyRequest.


        :param sampling_rate: The sampling_rate of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :type: str
        """
        if sampling_rate is None:
            raise ValueError("Invalid value for `sampling_rate`, must not be `None`")  # noqa: E501

        self._sampling_rate = sampling_rate

    @property
    def topn(self):
        """Gets the topn of this VoiceprinttopnVerifyRequest.  # noqa: E501


        :return: The topn of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :rtype: int
        """
        return self._topn

    @topn.setter
    def topn(self, topn):
        """Sets the topn of this VoiceprinttopnVerifyRequest.


        :param topn: The topn of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :type: int
        """
        if topn is None:
            raise ValueError("Invalid value for `topn`, must not be `None`")  # noqa: E501

        self._topn = topn

    @property
    def timestamp(self):
        """Gets the timestamp of this VoiceprinttopnVerifyRequest.  # noqa: E501


        :return: The timestamp of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this VoiceprinttopnVerifyRequest.


        :param timestamp: The timestamp of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

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
        if not isinstance(other, VoiceprinttopnVerifyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
