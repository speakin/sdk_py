#!/usr/bin/env python3

from speakin_voice_sdk.api import Api
from speakin_voice_sdk.session_api import SessionApi


def getRecordId(sApi, action):
    recordInfo = sApi.startRecord({
        "voice_bit_count": 16,
        "voice_rate": 16000,
        "voice_lang": "common-short",
        "data_format": "WAV",
        "target_action": action,
    })
    rs = sApi.openUploadRecordStream(recordInfo['record_id'])
    # 上传文件 测试用demo目录下的 501-1_5.wav 音频文件
    with open('501-1_5.wav', 'rb') as f:
        rs.write(f.read())
        print("文件正在上传中...")
    rs.done()
    print("上传文件成功...")
    return recordInfo

api = Api("speakin_test", "mr1imt1etu7ryets9eoergua87h0pa4n", "http://api3.speakin.mobi")
api.getUserApi().setAppUser({"user_id": "xx", "user_type": "PEOPLE", "valid": True})
sessionInfo = api.startSession({
    "user_id": "xx",
    "can_register": True,
    "can_verify": True,
    "can_identity": True,
})

if sessionInfo != None:
    sessionApi = SessionApi(sessionInfo["session_id"], sessionInfo["session_secret"], "http://api3.speakin.mobi")

    recordInfo = getRecordId(sessionApi, "REGISTER")


    recordIdList = []
    recordIdList.append(recordInfo['record_id'])
    recordIdListReq = {}
    recordIdListReq['record_id_list'] = recordIdList
    # 声纹注册
    sessionApi.register(recordIdListReq)
    print("声纹注册成功...")


    recordInfo = getRecordId(sessionApi, "VERIFY")
    recordIdListObj = {}
    recordIdListObj['record_id'] = recordInfo['record_id']

    # 声纹验证
    result = sessionApi.verify(recordIdListObj)
    print(result['score'], result['threshold_score'])
    if result['result']:
        print("声纹验证成功...")
    else:
        print("声纹验证失败...")

    recordInfo = getRecordId(sessionApi, "IDENTITY")

    recordIdListObj['record_id'] = recordInfo['record_id']

    # 声纹认证
    userIdList = sessionApi.identity(recordIdListObj)
    if userIdList != None:
        print("声纹认证成功...")
        print(userIdList)
    else:
        print("声纹认证失败...")

else:
    print("sessonInfo 获取失败...")
