#!/usr/bin/env python3

from .base import BaseApi
from . import const
from . import session_api_obj
import bson
import base64


class RecordStream(object):
    def __init__(self, sessionApi, recordId):
        self._sessionApi = sessionApi
        self._recordId = recordId
        self._indexId = 0

    def write(self, data):
        self._indexId += 1
        req = {
            "record_id": self._recordId,
            "index_id": self._indexId,
            "data":  data,
        }
        self._sessionApi.uploadRecordPart(req)

    def done(self):
        self._sessionApi.uploadRecordDone({
            "record_id": self._recordId,
        })

    def cancel(self):
        self._sessionApi.uploadRecordCancel({
            "record_id": self._recordId,
        })


class SessionApi(BaseApi):
    def __init__(self, sessionId, sessionSecret, baseUrl):
        super(SessionApi, self).__init__(sessionId, const.ID_TYPE_SESSION_ID, sessionSecret, baseUrl)



    def startRecord(self, req):
        """
        每次上传文件时都需要从服务器获得一个record
        req 请求参数，类型为dict,必须符合session_api_obj.StartRecordRequestSchema定义
        返回 符合session_api_obj.StartRecordResponseSchema定义\n
        you need to get a record from the server when you upload some files\n
        :param req:   conform to the definition of   'session_api_obj.StartRecordRequestSchema' , type: dictionary
        :return:  conform to the definition of  'session_api_obj.StartRecordResponseSchema' , type: dictionary
        """
        url = "{0}/v1/session/record/start".format(self._baseUrl)
        return self.callApi(url, req, session_api_obj.StartRecordRequestSchema(),
                            session_api_obj.StartRecordResponseSchema())



    def openUploadRecordStream(self, recordId):
        """
        上传文件时需要用recordId 打开一个上传的流
        recordId 请求参数，类型为str
        返回 RecordStream 上传文件流\n
        get a RecordStream  from a recordId\n
        :param recordId:  str
        :return:  RecordStream
        """
        return RecordStream(self, recordId)



    def uploadRecordPart(self, req):
        """
        上传一部分的文件
        req 请求参数，类型为dict,必须符合session_api_obj.UploadRecordPartRequestSchema
        返回 符合session_api_obj.UploadRecordPartResponseSchema\n
        :param req:   conform to the definition of   'session_api_obj.UploadRecordPartRequestSchema' , type: dictionary
        :return:  conform to the definition of  'session_api_obj.UploadRecordPartResponseSchema' , type: dictionary
        """
        url = "{0}/v1/session/record/upload_part".format(self._baseUrl)
        return self.callApi(url, req, session_api_obj.UploadRecordPartRequestSchema(),
                            session_api_obj.UploadRecordPartResponseSchema())



    def uploadRecordDone(self, req):
        """
        上传完成之后，关闭上传文件流
        req 请求参数，类型为dict,必须符合session_api_obj.UploadRecordDoneRequestSchema
        返回 符合session_api_obj.UploadRecordDoneResponseSchema\n
        close RecordStream when upload a file successfully\n
        :param req:   conform to the definition of   'session_api_obj.UploadRecordDoneRequestSchema' , type: dictionary
        :return:  conform to the definition of  'session_api_obj.UploadRecordDoneResponseSchema' , type: dictionary
        """
        url = "{0}/v1/session/record/done".format(self._baseUrl)
        return self.callApi(url, req, session_api_obj.UploadRecordDoneRequestSchema(),
                            session_api_obj.UploadRecordDoneResponseSchema())



    def uploadRecordCancel(self, req):
        """
        取消上传文件
        req 请求参数，类型为dict,必须符合session_api_obj.UploadRecordCancelRequestSchema
        返回 符合session_api_obj.UploadRecordCancelResponseSchema\n
        cancel uploading files\n
        :param req:   conform to the definition of   'session_api_obj.UploadRecordCancelRequestSchema' , type: dictionary
        :return:  conform to the definition of  'session_api_obj.UploadRecordCancelResponseSchema' , type: dictionary
        """
        url = "{0}/v1/session/record/cancel".format(self._baseUrl)
        return self.callApi(url, req, session_api_obj.UploadRecordCancelRequestSchema(),
                            session_api_obj.UploadRecordCancelResponseSchema())



    def register(self, req):
        """
        注册文件
        req 请求参数，类型为dict,必须符合session_api_obj.RegisterRequestSchema
        返回 符合session_api_obj.RegisterResponseSchema\n
        register files by recoredIds\n
        :param req:   conform to the definition of   'session_api_obj.RegisterRequestSchema' , type: dictionary
        :return:  conform to the definition of  'session_api_obj.RegisterResponseSchema' , type: dictionary
        """
        url = "{0}/v1/session/register".format(self._baseUrl)
        return self.callApi(url, req, session_api_obj.RegisterRequestSchema(), session_api_obj.RegisterResponseSchema())



    def verify(self, req):
        """
        验证文件
        req 请求参数，类型为dict,必须符合session_api_obj.VerifyRequestSchema
        返回 符合session_api_obj.VerifyResponseSchema\n
        verify file by recoredId\n
        :param req:   conform to the definition of   'session_api_obj.VerifyRequestSchema' , type: dictionary
        :return:  conform to the definition of  'session_api_obj.VerifyResponseSchema' , type: dictionary
        """
        url = "{0}/v1/session/verify".format(self._baseUrl)
        return self.callApi(url, req, session_api_obj.VerifyRequestSchema(), session_api_obj.VerifyResponseSchema())



    def identity(self, req):
        """
        认证文件
        req 请求参数，类型为dict,必须符合session_api_obj.IdentityRequestSchema
        返回 符合session_api_obj.IdentityResponseSchema\n
        identity file by recoredId\n
        :param req:   conform to the definition of   'session_api_obj.IdentityRequestSchema' , type: dictionary
        :return:  conform to the definition of  'session_api_obj.IdentityResponseSchema' , type: dictionary
        """
        url = "{0}/v1/session/identity".format(self._baseUrl)
        return self.callApi(url, req, session_api_obj.IdentityRequestSchema(), session_api_obj.IdentityResponseSchema())


if __name__ == "__main__":
    from .api import Api

    api = Api("speakin_test", "mr1imt1etu7ryets9eoergua87h0pa4n", "http://api3.speakin.mobi")
    api.getUserApi().setAppUser({"user_id": "xx", "user_type": "PEOPLE", "valid": True})
    sessionInfo = api.startSession({
        "user_id": "xxx",
        "can_register": True,
    })
    print(sessionInfo)
    sessionApi = SessionApi(sessionInfo["session_id"], sessionInfo["session_secret"], "http://api3.speakin.mobi")
    recordInfo = sessionApi.startRecord({
        "voice_bit_count": 16,
        "voice_rate": 16000,
        "voice_lang": "common-short",
        "data_format": "WAV",
        "target_action": "REGISTER",
    })
    print(recordInfo)
