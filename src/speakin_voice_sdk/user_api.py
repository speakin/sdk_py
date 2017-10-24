from .base import BaseApi
from . import const
from . import user_api_obj


class UserApi(BaseApi):
    def __init__(self, appId, appSecret, baseUrl):
        super(UserApi, self).__init__(appId, const.ID_TYPE_APP_ID, appSecret, baseUrl)



    def setAppUser(self, req):
        """
        添加或修改用户
        req 请求参数，类型为dict,必须符合user_api_obj.SetAppUserRequestSchema
        返回 符合user_api_obj.SetAppUserResponseSchema\n
        add or update user's info\n
        :param req:   conform to the definition of   'user_api_obj.SetAppUserRequestSchema' , type: dictionary
        :return:  conform to the definition of  'user_api_obj.SetAppUserResponseSchema' , type: dictionary
        """
        url = "{0}/v1/user/set".format(self._baseUrl)
        return self.callApi(url, req, user_api_obj.SetAppUserRequestSchema(), user_api_obj.SetAppUserResponseSchema())



    def getAppUser(self, req):
        """
        获取用户信息
        req 请求参数，类型为dict,必须符合user_api_obj.GetAppUserRequestSchema
        返回 符合user_api_obj.GetAppUserResponseSchema\n
        get user's info\n
        :param req:   conform to the definition of   'user_api_obj.GetAppUserRequestSchema' , type: dictionary
        :return:  conform to the definition of  'user_api_obj.GetAppUserResponseSchema' , type: dictionary
        """
        url = "{0}/v1/user/get".format(self._baseUrl)
        return self.callApi(url, req, user_api_obj.GetAppUserRequestSchema(), user_api_obj.GetAppUserResponseSchema())



    def addChildAppUser(self, req):
        """
        添加子用户
        req 请求参数，类型为dict,必须符合user_api_obj.AddChildAppUserRequestSchema
        返回 符合user_api_obj.AddChildAppUserResponseSchema\n
        :param req:   conform to the definition of   'user_api_obj.AddChildAppUserRequestSchema' , type: dictionary
        :return:  conform to the definition of  'user_api_obj.AddChildAppUserResponseSchema' , type: dictionary
        """
        url = "{0}/v1/user/add_child".format(self._baseUrl)
        return self.callApi(url, req, user_api_obj.AddChildAppUserRequestSchema(),
                            user_api_obj.AddChildAppUserResponseSchema())



    def removeChildAppUser(self, req):
        """
        删除子用户
        req 请求参数，类型为dict,必须符合user_api_obj.RemoveChildAppUserRequestSchema
        返回 符合user_api_obj.RemoveChildAppUserResponseSchema\n
        :param req:   conform to the definition of   'user_api_obj.RemoveChildAppUserRequestSchema' , type: dictionary
        :return:  conform to the definition of  'user_api_obj.RemoveChildAppUserResponseSchema' , type: dictionary
        """
        url = "{0}/v1/user/remove_child".format(self._baseUrl)
        return self.callApi(url, req, user_api_obj.RemoveChildAppUserRequestSchema(),
                            user_api_obj.RemoveChildAppUserResponseSchema())



    def getChildAppUserCount(self, req):
        """
        获取子用户的数量
        req 请求参数，类型为dict,必须符合user_api_obj.GetChildAppUserCountRequestSchema
        返回 符合user_api_obj.GetChildAppUserCountResponseSchema\n
        get the count of user's child(user)\n
        :param req:   conform to the definition of   'user_api_obj.GetChildAppUserCountRequestSchema' , type: dictionary
        :return:  conform to the definition of  'user_api_obj.GetChildAppUserCountResponseSchema' , type: dictionary
        """
        url = "{0}/v1/user/get_child_count".format(self._baseUrl)
        return self.callApi(url, req, user_api_obj.GetChildAppUserCountRequestSchema(),
                            user_api_obj.GetChildAppUserCountResponseSchema())



    def listChildAppUser(self, req):
        """
        列出子用户
        req 请求参数，类型为dict,必须符合user_api_obj.ListChildAppUserRequestSchema
        返回 符合user_api_obj.ListChildAppUserResponseSchema\n
        list  user's children(users)\n
        :param req:   conform to the definition of   'user_api_obj.ListChildAppUserRequestSchema' , type: dictionary
        :return:  conform to the definition of  'user_api_obj.ListChildAppUserResponseSchema' , type: dictionary
        """
        url = "{0}/v1/user/list_child".format(self._baseUrl)
        return self.callApi(url, req, user_api_obj.ListChildAppUserRequestSchema(),
                            user_api_obj.ListChildAppUserResponseSchema())



    def containChildAppUser(self, req):
        """
        检验是否包含子用户
        req 请求参数，类型为dict,必须符合user_api_obj.ContainChildAppUserRequestSchema
        返回 符合user_api_obj.ContainChildAppUserResponseSchema\n
        whether or not children of user contains user.\n
        :param req:   conform to the definition of   'user_api_obj.ContainChildAppUserRequestSchema' , type: dictionary
        :return:  conform to the definition of  'user_api_obj.ContainChildAppUserResponseSchema' , type: dictionary
        """
        url = "{0}/v1/user/contain_child".format(self._baseUrl)
        return self.callApi(url, req, user_api_obj.ContainChildAppUserRequestSchema(),
                            user_api_obj.ContainChildAppUserResponseSchema())

# if __name__ == "__main__":
#     from api import Api
#     api = Api("speakin_test","mr1imt1etu7ryets9eoergua87h0pa4n", "http://api2.speakin.mobi")
#     userApi = api.getUserApi()
#     userApi.setAppUser({"user_id":"xx","user_type":"PEOPLE"})
