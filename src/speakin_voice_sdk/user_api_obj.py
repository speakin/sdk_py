#!/usr/bin/env python3

from marshmallow import Schema, fields

class SetAppUserRequestSchema(Schema):
    user_id = fields.Str(required=True)
    user_type = fields.Str(required=True)
    valid = fields.Bool(default=False)
    access_all_app_user = fields.Bool(default=False)

class SetAppUserResponseSchema(Schema):
    pass

class GetAppUserRequestSchema(Schema):
    user_id = fields.Str(required=True)

class GetAppUserResponseSchema(Schema):
    user_id = fields.Str(required=True)
    user_type = fields.Str(required=True)
    valid = fields.Bool(default=False)
    access_all_app_user = fields.Bool(default=False)

class AddChildAppUserRequestSchema(Schema):
    user_id = fields.Str(required=True)
    child_user_id = fields.Str(required=True)

class AddChildAppUserResponseSchema(Schema):
    pass

class RemoveChildAppUserRequestSchema(Schema):
    user_id = fields.Str(required=True)
    child_user_id = fields.Str(required=True)

class RemoveChildAppUserResponseSchema(Schema):
    pass

class GetChildAppUserCountRequestSchema(Schema):
    user_id = fields.Str(required=True)

class GetChildAppUserCountResponseSchema(Schema):
    count = fields.Int(required=True)

class ListChildAppUserRequestSchema(Schema):
    user_id = fields.Str(required=True)
    offset = fields.Int(required=True)
    limit = fields.Int(required=True)

class ListChildAppUserResponseSchema(Schema):
    child_user_id_list = fields.List(fields.Str(), required=True)

class ContainChildAppUserRequestSchema(Schema):
    user_id = fields.Str(required=True)
    child_user_id = fields.Str(required=True)

class ContainChildAppUserResponseSchema(Schema):
    contain = fields.Bool(required=True)
