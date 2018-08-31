import hashlib
import hmac
import base64
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode,parse_qsl


class BucketTokenMiddleware(object):
    """
    use to add bucket token
    """
    def __init__(self, pre_pool, access_key, secret_key):
        self.pre_pool = pre_pool
        self.access_key = access_key
        self.secret_key = secret_key

    def request(self, method, url, fields=None, headers=None, **urlopen_kw):
        uri = urlparse(url)
        query = parse_qs(uri.query, strict_parsing=True)
        s = "%s?%s" % (uri.path, uri.query)
        sha = hmac.new(self.secret_key.encode(), s.encode(), hashlib.sha1)
        digest = base64.urlsafe_b64encode(sha.digest())
        headers["Authorization"] = "SpeakIn " + self.access_key + ":" + digest.decode()
        #print("head: ", headers)

        return self.pre_pool.request(method, url, fields, headers, **urlopen_kw)


class ApiTokenMiddleware(object):
    """
    use to add api token
    """
    def __init__(self, pre_pool, access_key, secret_key):
        self.pre_pool = pre_pool
        self.access_key = access_key
        self.secret_key = secret_key

    def request(self, method, url, fields=None, headers=None, **urlopen_kw):
        body = urlopen_kw["body"]
        #print("body: ", body)
        sha1 = hmac.new(self.secret_key.encode(), body.encode("utf-8"), hashlib.sha1)
        digest = base64.urlsafe_b64encode(sha1.digest())
        headers["Authorization"] = "SpeakIn " + self.access_key + ":" + digest.decode()
        #print("head: ", headers)

        return self.pre_pool.request(method, url, fields, headers, **urlopen_kw)


