config = {
    "app": {
        "name": "app-test",
        "accessKey": "xxxxxxxxx",
        "secretKey": "xxxxxxxxx",
    },
    "bucket": {
        "name": "bucket-test",
        "accessKey": "xxxxxxxxx",
        "secretKey": "xxxxxxxx",
    },
    "unionID": "py_user1",
    "registerFiles": ["../testdata/text/u1/01_16k.wav", "../testdata/text/u1/02_16k.wav", "../testdata/text/u1/03_16k.wav"],
    "verifyFile": "../testdata/text/u1/04_16k.wav",
    "simpleRate": "16k"
}

config_digital = {
    "app": {
        "name": "app-test",
        "accessKey": "xxxxxxxxx",
        "secretKey": "xxxxxxxx",
    },
    "bucket": {
        "name": "bucket-test",
        "accessKey": "xxxxxxxxx",
        "secretKey": "xxxxxxxx",
    },
    "unionID": "py_user2",
    "registerFiles": ["../testdata/digital/u1/01_16k.wav", "../testdata/digital/u1/02_16k.wav", "../testdata/digital/u1/03_16k.wav"],
    "verifyFile": "../testdata/digital/u1/04_16k.wav",
    "simpleRate": "16k"
}
