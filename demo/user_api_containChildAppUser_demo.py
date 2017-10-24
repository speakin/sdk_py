#!/usr/bin/env python3

from speakin_voice_sdk.api import Api


api = Api("speakin_test","mr1imt1etu7ryets9eoergua87h0pa4n","http://api3.speakin.mobi")
# 获取用户管理接口
userApi = api.getUserApi()
# 检查是否包含子用户
isContain = userApi.containChildAppUser({"user_id":"xx","child_user_id":"xxx"})
print(isContain)