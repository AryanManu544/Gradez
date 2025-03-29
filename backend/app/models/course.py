from mongoengine import Document, StringField, DateTimeField, IntField, ListField, ReferenceField

class Course(Document):
    title = StringField(required=True)
    description = StringField()
    instructor_id = ReferenceField('User', required=True)
    category = StringField()
    tags = ListField(StringField())
    difficulty_level = StringField()
    estimated_duration = IntField()  # In minutes
    created_at = DateTimeField()
    updated_at = DateTimeField()
    status = StringField(choices=["draft", "published", "archived"])
    image = StringField()  # URL to course thumbnail
    popularity_score = IntField()  # You could also use FloatField if needed
    average_rating = IntField()    # Or FloatField if ratings include decimals

    meta = {'collection': 'courses'}
