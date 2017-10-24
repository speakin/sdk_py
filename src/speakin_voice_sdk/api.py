#!/usr/bin/env python3

from .base import BaseApi
from . import const
from . import api_obj
from .user_api import UserApi


class Api(BaseApi):
    def __init__(self, appId, appSecret, baseUrl):
        super(Api, self).__init__(appId, const.ID_TYPE_APP_ID, appSecret, baseUrl)

    def getUserApi(self):
        return UserApi(self._id, self._secret, self._baseUrl)



    def listModule(self, req):
        """
        列出所有模型
        req 请求参数，类型为dict,必须符合api_obj.ListModuleRequestSchema定义
        返回 符合api_obj.ListModuleResponeSchema定义\n
        :param req:   conform to the definition of  'api_obj.ListModuleRequestSchema' , type: dictionary
        :return:  conform to the definition of  'api_obj.ListModuleResponeSchema' , type: dictionary
        """
        url = "{0}/v1/list_module".format(self._baseUrl)
        return self.callApi(url, req, api_obj.ListModuleRequestSchema(), api_obj.ListModuleResponeSchema())



    def startSession(self, req):
        """
        req 请求参数，类型为dict,必须符合api_obj.StartSessionRequestSchema
        返回 符合api_obj.StartSessionResponseSchema定义\n
        :param req:   conform to the definition of   'api_obj.StartSessionRequestSchema' , type: dictionary
        :return:  conform to the definition of  'api_obj.StartSessionResponseSchema' , type: dictionary
        """
        url = "{0}/v1/start_session".format(self._baseUrl)
        return self.callApi(url, req, api_obj.StartSessionRequestSchema(), api_obj.StartSessionResponseSchema())

    def quertTrace(self, req, traceId):
        """
        查询日志
        :param req:
        :return:
        """
        url = "{0}/v1/query_trace?traceId={1}".format(self._baseUrl, traceId)
        return self.callApi(url, req, api_obj.QueryTraceRequest(), api_obj.QueryTraceResponse())

# if __name__ == "__main__":
#     api = Api("speakin_test","mr1imt1etu7ryets9eoergua87h0pa4n","http://api2.speakin.mobi")
#     res = api.listModule({})
#     print(res)
