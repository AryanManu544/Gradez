from mongoengine import Document, StringField, EmailField, DateTimeField, DictField

class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password_hash = StringField(required=True)
    first_name = StringField()
    last_name = StringField()
    role = StringField(choices=["student", "instructor", "admin"])
    created_at = DateTimeField()
    updated_at = DateTimeField()
    preferences = DictField()  # Expects keys: learning_style, difficulty_preference, interests, pace
    profile_image = StringField()  # URL to profile image

    meta = {'collection': 'users'}
