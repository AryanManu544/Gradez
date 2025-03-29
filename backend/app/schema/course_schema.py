from marshmallow import Schema, fields, validate

class CourseSchema(Schema):
    id = fields.String(dump_only=True)  # Serialized ObjectId
    title = fields.String(required=True)
    description = fields.String()
    instructor_id = fields.String(required=True)
    category = fields.String()
    tags = fields.List(fields.String())
    difficulty_level = fields.String()
    estimated_duration = fields.Integer()  # In minutes
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    status = fields.String(validate=validate.OneOf(["draft", "published", "archived"]))
    image = fields.String()  # URL to course thumbnail
    popularity_score = fields.Integer()
    average_rating = fields.Float()
