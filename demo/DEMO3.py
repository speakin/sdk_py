#!/usr/bin/env python3
import os, csv, codecs, datetime
import threading

import _thread
from concurrent.futures import ThreadPoolExecutor

import sys

from speakin_voice_sdk.api import Api
from speakin_voice_sdk.session_api import SessionApi

# 常量#constants
OUT_FILE_NAME = 'report.csv'  # Generate results. Only .csv files are supported.
BASE_FILE_NAME = 'sdk_test_voice/' #Test directory
REGISTER_FILE_NAME = "/register/"   #Folder for registered files.
VERIFY_FILE_NAME = "/verify/"  #Folder for verified files
URL = "http://api3.speakin.mobi" #server ip
#URL = "http://api2.speakin.mobi" #server ip


# 讲执行结果写入文档#The execution results are written to the document
def report(values):
    lock = _thread.allocate_lock()
    lock.acquire()
    lock.locked()
    csvFile = open(OUT_FILE_NAME, 'a', newline='')
    for value in values:
        csvFile.write(codecs.BOM_UTF8.decode('utf-8'))
        writer = csv.writer(csvFile)
        writer.writerow(value)
    csvFile.close()  # 上传文件#upload files
    lock.release()


def uploadFile(fileName, record_id, sessionApi):
    rs = sessionApi.openUploadRecordStream(record_id)
    with open(fileName, 'rb') as f:
        print(fileName)
        rs.write(f.read())
        #print("The document is being circulated...")
        print("文件正在上传中...")
    rs.done()
    #print("Upload file success...")
    print("上传文件成功...")


# 声纹注册#Voice print registration
def register(recordIdList, sessionApi):
    recordIdListReq = {}
    recordIdListReq['record_id_list'] = recordIdList
    # 声纹注册#Voice print registration
    sessionApi.register(recordIdListReq)
    #print("Register Successfully...")
    print("声纹注册成功...")


def getSessionApi(userId):
    api = Api("speakin_test", "mr1imt1etu7ryets9eoergua87h0pa4n", URL)
    api.getUserApi().setAppUser({"user_id": userId, "user_type": "PEOPLE", "valid": True})
    sessionInfo = api.startSession({
        "user_id": userId,
        "can_register": True,
        "can_verify": True,
        "can_identity": True,
    })
    return SessionApi(sessionInfo["session_id"], sessionInfo["session_secret"],
                      URL)


def getRecordInfo(sessionApi, action):
    return sessionApi.startRecord({
        "voice_bit_count": 16,
        "voice_rate": 16000,
        "voice_lang": "common-short",  # number-highthres,common-short,eddy_long
        "data_format": "WAV",
        "target_action": action,
    })


# 注册#register
def registerFile(registerFileName, userId, excels):
    starttime = datetime.datetime.now()
    if not os.path.exists(registerFileName):
        #print(registerFileName, "Files or folders do not exist")
        print(registerFileName, "文件或文件夹不存在")
        return
    files1 = os.listdir(registerFileName)
    recordIdList = []

    sessionApi = getSessionApi(userId)
    for i in files1:
        registerTNum = 1
        verifyTNum = '-'
        falseFile = '-'
        score = thresholdScore = dyanmicCmpScore = 0
        uploadtimeStart = datetime.datetime.now()
        try:
            if i[0] == '.':
                continue
            if sessionApi != None:
                recordInfo = getRecordInfo(sessionApi, "REGISTER")
                # 上传文件#upload files
                uploadFile(registerFileName + i, recordInfo['record_id'], sessionApi)
                recordIdList.append(recordInfo['record_id'])
                uploadtimeEnd = datetime.datetime.now()
                uploadCost = (uploadtimeEnd - uploadtimeStart).microseconds

            else:
                registerTNum = 0
                #print("recordInfo fails to read...")
                print("recordInfo 获取失败...")
        except:
            registerTNum = 0
        endtime = datetime.datetime.now()
        cost = (endtime - starttime).microseconds
        excels.append(
            [userId, registerTNum, verifyTNum, falseFile, score, thresholdScore, dyanmicCmpScore, i, cost, ''])
    if len(recordIdList) == 0:
        #print(BASE_FILE_NAME + userId + "/----> No files in the directory", )
        print(BASE_FILE_NAME + userId + "/----> 目录下没有文件", )
    else:
        # 声纹统一注册#Unified voice print registration
        register(recordIdList, sessionApi)


# 验证#verify
def verifyFile(verifyFileNames, registerFileName, userId, excels):
    starttime = datetime.datetime.now()
    count = 0
    failCount = 0
    for verifyFileName in verifyFileNames:
        if not os.path.exists(verifyFileName):
            #print(verifyFileName, "Files or folders do not exist")
            print(verifyFileName, "文件或文件夹不存在")
            continue
        # 去掉它本身的注册文件#Get rid of its own registry file
        if verifyFileName == registerFileName:
            continue
        files2 = os.listdir(verifyFileName)
        for i in files2:
            registerTNum = '-'
            verifyTNum = score = thresholdScore = falseFile = dyanmicCmpScore = 0
            try:
                if i[0] == '.':
                    continue
                sessionApi = getSessionApi(userId)
                # 上传文件#upload files
                recordInfo = getRecordInfo(sessionApi, "VERIFY")
                uploadFile(verifyFileName + i, recordInfo['record_id'], sessionApi)
                print("Upload successfully...")
                #print("声纹上传成功...")

                # 声纹验证#Voiceprint authentication
                recordIdListObj = {}
                recordIdListObj['record_id'] = recordInfo['record_id']
                verify = sessionApi.verify(recordIdListObj)
                score = verify['score']
                thresholdScore = verify['threshold_score']
                dyanmicCmpScore = verify['dynamiccmpscore']
                if verify['result']:
                    verifyTNum = 1
                    #print(verifyFileName + i, "Successful voice print verification...")
                    print(verifyFileName + i, "声纹验证成功...")
                else:
                    verifyTNum = 0
                    falseFile = 0
                    #print("Voiceprint validation failed...")
                    print("声纹验证失败...")
                    # falseFile.append(i)  #打印失败的文件#Print failed files

                recordInfo = getRecordInfo(sessionApi, "IDENTITY")
                uploadFile(verifyFileName + i, recordInfo['record_id'], sessionApi)
                recordIdListObj['record_id'] = recordInfo['record_id']
                # 声纹认证#Voiceprint authentication
                userIdList = sessionApi.identity(recordIdListObj)
                if len(userIdList['user_id_list']) != 0:
                    falseFile = 1
                    #print(verifyFileName + i, "Authenticate voiceprint successfully...")
                    print(verifyFileName + i, "声纹认证成功...")
                else:
                    falseFile = 0
                    failCount += 1
                    #print(verifyFileName + i, "Authenticate voiceprint failed...")
                    print(verifyFileName + i, "声纹认证失败...")
            except Exception as e:
                print(e)
                falseFile = 0
                failCount += 1
            count += 1
            endtime = datetime.datetime.now()
            cost = (endtime - starttime).microseconds
            excels.append(
                [userId, registerTNum, verifyTNum, falseFile, score, thresholdScore, dyanmicCmpScore, i, cost, ''])
    excels.append([userId, '', '', '', '', '', '失败的次数', failCount, '验证的总次数：', count])
    #excels.append([userId, '', '', '', '', '', 'Failure Tasks', failCount, 'Attempts', count])
    report(excels)


# 获取所有的验证文件路径#Gets all the validation file paths
def getVerifyFileNames(dirs):
    verifyFileNames = []
    for userId in dirs:
        registerFileName = BASE_FILE_NAME + userId + REGISTER_FILE_NAME
        verifyFileName = BASE_FILE_NAME + userId + VERIFY_FILE_NAME
        verifyFileNames.append(registerFileName)
        verifyFileNames.append(verifyFileName)
    return verifyFileNames


# 删除文件#Delete the file
def removeFile(fileName):
    try:
        os.remove(fileName)
    except:
        pass


# 注册和认证
def worker(userId):
    excels = [[]]
    #excels.append(['users:' + userId + ', Registered Files：', '', '', '', '', '', '', '', '', ''])
    excels.append(['用户:' + userId + ',注册文件：', '', '', '', '', '', '', '', '', ''])
    registerFileName = BASE_FILE_NAME + userId + REGISTER_FILE_NAME
    verifyFileNames = [BASE_FILE_NAME + userId + VERIFY_FILE_NAME]
    registerFile(registerFileName, userId, excels)
    #excels.append(['users:' + userId + ',Verified Files：', '', '', '', '', '', '', '', '', ''])
    excels.append(['用户:' + userId + ',验证文件：', '', '', '', '', '', '', '', '', ''])
    verifyFile(verifyFileNames, registerFileName, userId, excels)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        BASE_FILE_NAME = sys.argv[1] + "/"
    # 删除之前的文件#Delete the previous file
    removeFile(OUT_FILE_NAME)
    #report([['User', 'Registration Status', 'Verification Status', 'Identity Status', 'Score','Threshold', 'Dynamic Threshold', 'Response Time(ms)', 'File Name','Times of Attempt']])
    report([['名称', '注册是否成功', '验证是否成功', '', '得分', '阈值', '动态阈值', '响应时间(微秒)', '文件名', '验证的次数']])
    if not os.path.exists(BASE_FILE_NAME):
        #print(BASE_FILE_NAME, "Files or folders do not exist")
        print(BASE_FILE_NAME, "文件或文件夹不存在")
        exit(0)
    dirs = os.listdir(BASE_FILE_NAME)
    verifyFileNames = getVerifyFileNames(dirs)
    pool = ThreadPoolExecutor(max_workers=100)
    for userId in dirs:
        if userId[0] == '.':
            continue
        else:
            pool.submit(worker, (userId))
