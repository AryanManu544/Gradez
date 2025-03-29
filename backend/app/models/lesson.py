from mongoengine import Document, StringField, DateTimeField, IntField, DictField, ReferenceField

class Lesson(Document):
    course_id = ReferenceField('Course', required=True)
    title = StringField(required=True)
    description = StringField()
    order = IntField()  # Order in the course
    content_type = StringField(choices=["video", "text", "interactive", "quiz"])
    content = DictField()  # Expect keys: text, video_url, interactive_data
    duration = IntField()  # In minutes
    created_at = DateTimeField()
    updated_at = DateTimeField()

    meta = {'collection': 'lessons'}
