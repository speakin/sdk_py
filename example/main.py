import time

import openapi_client
from tok import ApiTokenMiddleware, BucketTokenMiddleware
from config import config

conf = config
configuration = openapi_client.Configuration()


def get_voiceprint_cli(access_key, secret_key):
    api_client = openapi_client.ApiClient(configuration=configuration)
    pool = api_client.rest_client.pool_manager
    api_client.rest_client.pool_manager = ApiTokenMiddleware(
        pool, access_key, secret_key)
    return openapi_client.VoiceprintApi(api_client=api_client)


voiceprint_api = get_voiceprint_cli(conf['app']['accessKey'],
                                    conf['app']['secretKey'])


def get_storage_cli(access_key, secret_key):
    api_client = openapi_client.ApiClient(configuration=configuration)
    pool = api_client.rest_client.pool_manager
    api_client.rest_client.pool_manager = BucketTokenMiddleware(
        pool, access_key, secret_key)
    return openapi_client.StorageApi(api_client=api_client)


storage_api = get_storage_cli(conf['bucket']['accessKey'],
                              conf['bucket']['secretKey'])


def query_threshold(app_name):
    req = openapi_client.VoiceprintThresholdRequest(
                app_name=app_name,
                timestamp=int(time.time())
            )
    resp = voiceprint_api.threshold(voiceprint_threshold_request=req)
    if resp.has_error:
        raise Exception(resp)
    return resp.data.threshold


def upload_file(filename):
    return upload_files([filename])[0]


def upload_files(filenames):
    keys = []
    for name in filenames:
        ts = int(time.time())
        f = open(name, 'rb')
        content = f.read()
        f.close()
        resp = storage_api.upload(conf['bucket']['name'], 'wav', ts, **{
            'body': content,
        })
        if resp.has_error:
            raise Exception(resp)
        keys.append(resp.data.key)
    return keys


def register(app_name, union_id, keys, simpleRate):
    req = openapi_client.VoiceprintRegisterRequest(
        app_name=app_name,
        replace=True,
        union_id=union_id,
        urls=keys,
        sampling_rate=simpleRate,
        timestamp=int(time.time()),
    )
    resp = voiceprint_api.register(voiceprint_register_request=req)
    if resp.has_error:
        raise Exception(resp)


def verify(app_name, union_id, key, simpleRate):
    req = openapi_client.VoiceprintVerifyRequest(
        app_name=app_name,
        union_id=union_id,
        url=key,
        sampling_rate=simpleRate,
        timestamp=int(time.time()),
    )
    resp = voiceprint_api.verify(voiceprint_verify_request=req)
    if resp.has_error:
        raise Exception(resp)
    return resp.data.score


def query(app_name, union_id):
    req = openapi_client.VoiceprintQueryRequest(
        app_name=app_name,
        timestamp=int(time.time()),
        union_id=union_id
    )
    resp = voiceprint_api.query(voiceprint_query_request=req)
    if resp.has_error:
        raise Exception(resp)

    return resp.data.is_register


def main():
    try:
        # 查询阈值
        threshold = query_threshold(conf['app']['name'])
        print('threshold:', threshold)
        # 查询
        is_register = query(conf['app']['name'], conf['unionID'])
        print('is_register:', is_register)
        # 上传注册文件
        keys = upload_files(conf['registerFiles'])
        print('register keys:', keys)
        # 注册
        register(conf['app']['name'], conf['unionID'], keys,
                 conf['simpleRate'])
        # 查询
        is_register = query(conf['app']['name'], conf['unionID'])
        print('is_register:', is_register)
        # 上传验证文件
        key = upload_file(conf['verifyFile'])
        print('verify key:', key)
        # 验证
        score = verify(conf['app']['name'], conf['unionID'], key,
                       conf['simpleRate'])
        print('score:', score)

    except Exception as e:
        print('Exception when calling %s' % e)


if __name__ == '__main__':
    main()
