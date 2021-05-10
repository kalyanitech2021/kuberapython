import mongoengine as db

class User(db.Document):
    user_id = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, min_length=8, max_length=12)
    firstname = db.StringField()
    lastname = db.StringField()
    def to_json(self):
        return {"user_id": self.user_id,
                "password": self.password}
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)