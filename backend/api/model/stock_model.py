import mongoengine_goodjson as gj
import mongoengine as db

class Stock(gj.Document):
    user_id = db.StringField()
    transaction_date = db.StringField()
    transaction_type = db.StringField()
    symbol = db.StringField()
    quantity = db.IntField()
    price = db.IntField()