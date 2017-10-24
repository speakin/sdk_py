#!/usr/bin/env python3

from marshmallow import Schema, fields

class StartSessionRequestSchema(Schema):
    user_id = fields.Str(required=True,default="")
    can_register = fields.Bool(default=False)
    can_verify = fields.Bool(default=False)
    can_identity = fields.Bool(default=False)
    ttl = fields.Int(default=500)

class StartSessionResponseSchema(Schema):
    session_id = fields.Str(required=True)
    expire_time_stamp = fields.Int(required=True)
    session_secret = fields.Str(required=True)

class ListModuleRequestSchema(Schema):
    pass

class ModuleSchema(Schema):
    voice_bit_count = fields.Int(required=True)
    voice_rate = fields.Int(required=True)
    voice_lang = fields.Str(required=True)

class ListModuleResponeSchema(Schema):
    module_list = fields.List(fields.Nested(ModuleSchema),required=True)

class QueryTraceRequest(Schema):
    offset = fields.Int(required=True)
    limit = fields.Int(required=True)

class QueryTraceResponse(Schema):
    totalCount = fields.Int(required=True)
    logContent = fields.Str(required=True)