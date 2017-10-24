#!/usr/bin/env python3

from speakin_voice_sdk.api import Api


api = Api("speakin_test","mr1imt1etu7ryets9eoergua87h0pa4n","http://api3.speakin.mobi")
result = api.quertTrace({"offset": 0, "limit": 20}, "xxxyyyzzz")
print(result)
