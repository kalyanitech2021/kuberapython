import mongoengine as db

class User(db.Document):
    user_id = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, min_length=8, max_length=12)
    firstname = db.StringField()
    lastname = db.StringField()