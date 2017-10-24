#!/usr/bin/env python3
import bson
from Crypto.Cipher import AES
from Crypto.Hash import SHA
from Crypto import Random
import hashlib
import base64

def pkcs5Padding(s):
    p = (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
    return s + p.encode("utf8")

def pkcs5UnPaddings(s):
    return s[0:-(s[-1])]

def aesCrypt(secret, content):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(secret.encode("utf8"),AES.MODE_CBC,iv)
    msg = iv+cipher.encrypt(pkcs5Padding(content))
    # return base64.standard_b64encode(msg)
    return msg

def sign(content1, content2, content3):
    h = SHA.new()
    h.update(content1.encode("utf8"))
    h.update(content2)
    h.update(content3.encode("utf8"))
    # return base64.standard_b64encode(h.digest())
    return h.digest()
def aesDecrypt(secret, content):
    # content = base64.standard_b64decode(content)
    iv = content[:AES.block_size]
    content = content[AES.block_size:]
    cipher = AES.new(secret.encode("utf8"),AES.MODE_CBC,iv)
    content = cipher.decrypt(content)
    return pkcs5UnPaddings(content)
