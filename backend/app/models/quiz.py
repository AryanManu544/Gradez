from mongoengine import Document, StringField, DateTimeField, IntField, ListField, DictField, ReferenceField

class Quiz(Document):
    lesson_id = ReferenceField('Lesson', required=True)
    title = StringField(required=True)
    description = StringField()
    questions = ListField(DictField())  # Each dict can have keys: question, options, correct_answer, explanation
    passing_score = IntField()  # Percentage needed to pass
    created_at = DateTimeField()
    updated_at = DateTimeField()

    meta = {'collection': 'quizzes'}
