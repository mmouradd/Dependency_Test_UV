"""
Marshmallow schemas for validating post data.
"""

from marshmallow import Schema, fields


class PostSchema(Schema):
    userId = fields.Int(required=True)
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    body = fields.Str(required=True)


class PostSummarySchema(Schema):
    userId = fields.Int(required=True)
    post_count = fields.Int(required=True)
