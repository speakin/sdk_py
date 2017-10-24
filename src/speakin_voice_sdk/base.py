#!/usr/bin/env python3

from abc import ABCMeta

import bson
import requests
from datetime import datetime
from . import util
from marshmallow import Schema, fields


class ApiException(Exception):
    def __init__(self, error):
        self.error = error


class RequestWarp(object):
    def __init__(self, idStr, idTypeStr, secret):
        self._id = idStr
        self._idType = idTypeStr
        self._secret = secret

    def setData(self, bsonData):
        self._data = bson.dumps(bsonData)

    def genReqBody(self):
        callTimeStamp = int(datetime.now().timestamp() * 1000)
        encData = util.aesCrypt(self._secret, self._data)
        signContent1 = "{0}{1}{2}".format(self._id, self._idType, callTimeStamp)
        signContent2 = self._data
        signContent3 = self._secret
        sign = util.sign(signContent1, signContent2, signContent3)
        return bson.dumps({
            "id": self._id,
            "id_type": self._idType,
            "t": callTimeStamp,
            "data": encData,
            "sign": sign,
            "skip_crypt": False
        })


class ApiErrorSchema(Schema):
    errorId = fields.Str(attribute="id", default="", missing="")
    desc = fields.Str(default="", missing="")


class ResponseWarpSchema(Schema):
    has_error = fields.Bool(required=True)
    error = fields.Nested(ApiErrorSchema())
    data = fields.Str()
    t = fields.Int()
    sign = fields.Str()


class ResponseWarp(object):
    def __init__(self, secret, bodyStr):
        self._secret = secret

        resp = bson.loads(bodyStr)

        if resp["error"]['desc'] != '':
            raise ApiException({
                "id": "common.unkwon",
                "desc": resp["error"]["desc"],
            })
        self.has_error = resp["has_error"]
        self._sign = resp["sign"]
        self._execTime = resp["t"]
        self.error = resp["error"]
        if self.has_error and self.error["id"].startswith("common."):
            raise ApiException(self.error)
        self._data = util.aesDecrypt(self._secret, resp["data"])
        # self._data = self._data

    def getData(self):
        return self._data

    def checkSign(self):
        if self.has_error and self.error["id"].startswith("common."):
            raise ApiException(self.error)
        hasErrorStr = "false"
        if self.has_error:
            hasErrorStr = "true"
        signContent1 = "{0}{1}{2}{3}".format(self._execTime, hasErrorStr,
                                                  self.error["id"], self.error["desc"])
        signContent2 = self._data
        signContent3 = self._secret
        sign = util.sign(signContent1, signContent2, signContent3)
        if sign != self._sign:
            self.has_error = True
            self.error = {
                "id": "common.wrong_sign",
                "desc": "wrong sign",
            }


class BaseApi(object):
    __metaclass__ = ABCMeta

    def __init__(self, idStr, idTypeStr, secret, baseUrl):
        self._id = idStr
        self._idType = idTypeStr
        self._secret = secret
        self._baseUrl = baseUrl

    def callApi(self, url, req, reqSchema, respSchema):
        reqWarp = RequestWarp(self._id, self._idType, self._secret)
        _, errors = reqSchema.dump(req)
        if errors:
            raise ApiException({
                "id": "common.unkwon",
                "desc": str(errors),
            })

        reqWarp.setData(req)
        r = requests.post(url, data=reqWarp.genReqBody())
        resWarp = ResponseWarp(self._secret, r.content)
        _, errors = respSchema.dump(resWarp)
        if errors:
            raise ApiException({
                "id": "common.unkwon",
                "desc": str(errors),
            })
        resWarp.checkSign()
        ret = bson.loads(resWarp.getData())
        return ret
