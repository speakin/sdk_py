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
        'urls': 'list[str]',
        'sampling_rate': 'str',
        'topn': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'app_name': 'appName',
        'urls': 'urls',
        'sampling_rate': 'samplingRate',
        'topn': 'topn',
        'timestamp': 'timestamp'
    }

    def __init__(self, app_name=None, urls=None, sampling_rate=None, topn=None, timestamp=None):  # noqa: E501
        """VoiceprinttopnVerifyRequest - a model defined in OpenAPI"""  # noqa: E501

        self._app_name = None
        self._urls = None
        self._sampling_rate = None
        self._topn = None
        self._timestamp = None
        self.discriminator = None

        self.app_name = app_name
        self.urls = urls
        self.sampling_rate = sampling_rate
        self.topn = topn
        self.timestamp = timestamp

    @property
    def app_name(self):
        """Gets the app_name of this VoiceprinttopnVerifyRequest.  # noqa: E501

        应用名字  # noqa: E501

        :return: The app_name of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this VoiceprinttopnVerifyRequest.

        应用名字  # noqa: E501

        :param app_name: The app_name of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :type: str
        """
        if app_name is None:
            raise ValueError("Invalid value for `app_name`, must not be `None`")  # noqa: E501

        self._app_name = app_name

    @property
    def urls(self):
        """Gets the urls of this VoiceprinttopnVerifyRequest.  # noqa: E501

        文件url  # noqa: E501

        :return: The urls of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this VoiceprinttopnVerifyRequest.

        文件url  # noqa: E501

        :param urls: The urls of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :type: list[str]
        """
        if urls is None:
            raise ValueError("Invalid value for `urls`, must not be `None`")  # noqa: E501

        self._urls = urls

    @property
    def sampling_rate(self):
        """Gets the sampling_rate of this VoiceprinttopnVerifyRequest.  # noqa: E501

        sampling rate  # noqa: E501

        :return: The sampling_rate of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :rtype: str
        """
        return self._sampling_rate

    @sampling_rate.setter
    def sampling_rate(self, sampling_rate):
        """Sets the sampling_rate of this VoiceprinttopnVerifyRequest.

        sampling rate  # noqa: E501

        :param sampling_rate: The sampling_rate of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :type: str
        """
        if sampling_rate is None:
            raise ValueError("Invalid value for `sampling_rate`, must not be `None`")  # noqa: E501

        self._sampling_rate = sampling_rate

    @property
    def topn(self):
        """Gets the topn of this VoiceprinttopnVerifyRequest.  # noqa: E501

        top n  # noqa: E501

        :return: The topn of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :rtype: int
        """
        return self._topn

    @topn.setter
    def topn(self, topn):
        """Sets the topn of this VoiceprinttopnVerifyRequest.

        top n  # noqa: E501

        :param topn: The topn of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :type: int
        """
        if topn is None:
            raise ValueError("Invalid value for `topn`, must not be `None`")  # noqa: E501

        self._topn = topn

    @property
    def timestamp(self):
        """Gets the timestamp of this VoiceprinttopnVerifyRequest.  # noqa: E501

        时间戳  # noqa: E501

        :return: The timestamp of this VoiceprinttopnVerifyRequest.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this VoiceprinttopnVerifyRequest.

        时间戳  # noqa: E501

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
