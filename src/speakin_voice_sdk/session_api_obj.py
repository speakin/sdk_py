#!/usr/bin/env python3

from marshmallow import Schema, fields

class StartRecordRequestSchema(Schema):
    gen_text = fields.Bool(default=False)
    voice_bit_count = fields.Int(required=True)
    voice_rate = fields.Int(required=True)
    voice_lang = fields.Str(required=True)
    data_format = fields.Str(required=True)
    target_action = fields.Str(required=True)

class StartRecordResponseSchema(Schema):
    record_id = fields.Str(required=True)
    text = fields.Str(required=True)

class UploadRecordPartRequestSchema(Schema):
    record_id = fields.Str(required=True)
    index_id = fields.Int(required=True)
    data = fields.Raw(required=True)

class UploadRecordPartResponseSchema(Schema):
    pass

class UploadRecordDoneRequestSchema(Schema):
    record_id = fields.Str(required=True)

class UploadRecordDoneResponseSchema(Schema):
    pass

class UploadRecordCancelRequestSchema(Schema):
    record_id = fields.Str(required=True)

class UploadRecordCancelResponseSchema(Schema):
    pass

class RegisterRequestSchema(Schema):
    record_id_list = fields.List(fields.Str(),required=True)

class RegisterResponseSchema(Schema):
    pass

class VerifyRequestSchema(Schema):
    record_id = fields.Str(required=True)

class VerifyResponseSchema(Schema):
    result = fields.Bool(required=True)
    score  = fields.Float(required=True)
    threshold_score = fields.Float(required=True)
    dyanmic_cmp_score = fields.Float(required=True)

class IdentityRequestSchema(Schema):
    record_id = fields.Str(required=True)

class IdentityResponseSchema(Schema):
    user_id_list = fields.List(fields.Str(),required=True)
