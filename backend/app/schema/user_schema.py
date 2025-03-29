from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.String(dump_only=True)  # Serialized ObjectId
    username = fields.String(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    first_name = fields.String()
    last_name = fields.String()
    role = fields.String(validate=validate.OneOf(["student", "instructor", "admin"]))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    preferences = fields.Dict()  # Contains learning_style, difficulty_preference, interests, pace
    profile_image = fields.String()  # URL to profile image
