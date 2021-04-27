from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MONGODB_SETTINGS'] = {
    'db': 'StockDBPython',
    'host':'localhost',
    'port': 27017
    }

from route.users_route import *
from route.stock_route import *
from route.dividend_route import *
from route.portfolio_route import *

db = MongoEngine()
db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)