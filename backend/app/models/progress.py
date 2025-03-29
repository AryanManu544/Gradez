from mongoengine import Document, DateTimeField, BooleanField, IntField, ListField, ReferenceField

class Progress(Document):
    user_id = ReferenceField('User', required=True)
    course_id = ReferenceField('Course', required=True)
    lessons_completed = ListField(ReferenceField('Lesson'))
    quizzes_completed = ListField(ReferenceField('Quiz'))
    score = IntField()  # Overall score in percentage
    last_accessed = DateTimeField()
    completed = BooleanField(default=False)
    completion_date = DateTimeField()

    meta = {'collection': 'progress'}
