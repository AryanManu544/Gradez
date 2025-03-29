from mongoengine import Document, StringField, DateTimeField, DictField, ReferenceField

class UserActivity(Document):
    user_id = ReferenceField('User', required=True)
    activity_type = StringField(required=True)  # e.g., "login", "course_view", etc.
    metadata = DictField()  # Additional activity data
    timestamp = DateTimeField(required=True)

    meta = {'collection': 'user_activity'}
