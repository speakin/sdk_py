#!/usr/bin/env python3
import bson

from speakin_voice_sdk.api import Api


api = Api("speakin_test","mr1imt1etu7ryets9eoergua87h0pa4n","http://api3.speakin.mobi")
# 获取用户管理接口
userApi = api.getUserApi()
# 获取用户
user = userApi.getAppUser({"user_id":"xx"})

print(user["user_id"])
