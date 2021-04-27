import mongoengine_goodjson as gj
import mongoengine as db

class Dividend(gj.Document):
    user_id = db.StringField()
    transaction_date = db.StringField()
    transaction_type = db.StringField()
    symbol = db.StringField()
    ex_div_date = db.StringField()
    record_date = db.StringField()
    payment_date = db.StringField()
    quantity = db.IntField()
    div_per_share = db.FloatField()
    total_dividend = db.FloatField()