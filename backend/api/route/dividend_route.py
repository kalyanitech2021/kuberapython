from app import app
from controller.dividend_controller import DividendController

class DividendRoute:

    def __init__(self):
        print("Dividend Route Class Initialization")

    @app.route('/dividends', methods=['POST'])
    def add_dividend():
        return DividendController.add_dividend()

    @app.route('/dividends/<userId>/list')
    def get_all_dividends(userId):
        return DividendController.get_all_dividends(userId)

    @app.route('/dividends/<id>')
    def get_one_dividend(id):
        return DividendController.get_one_dividend(id)

    @app.route('/dividends/<id>/update', methods=['PUT'])
    def update_one_dividend(id):
        return DividendController.update_one_dividend(id)

    @app.route('/dividends/<id>/delete', methods=['DELETE'])
    def delete_one_dividend(id):
        return DividendController.delete_one_dividend(id)

    @app.route('/dividends/delete', methods=['DELETE'])
    def delete_all_dividends():
        return DividendController.delete_all_dividends()