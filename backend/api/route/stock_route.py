from app import app
from controller.stock_controller import StockController

class StockRoute:

    def __init__(self):
        print("Stock Route Class Initialization")

    @app.route('/stocks', methods=['POST'])
    def add_stock():
        return StockController.add_stock()

    @app.route('/stocks/<userId>/list')
    def get_all_stocks(userId):
        return StockController.get_all_stocks(userId)

    @app.route('/stocks/<id>')
    def get_one_stock(id):
        return StockController.get_one_stock(id)

    @app.route('/stocks/<id>/update', methods=['PUT'])
    def update_one_stock(id):
        return StockController.update_one_stock(id)

    @app.route('/stocks/<id>/delete', methods=['DELETE'])
    def delete_one_stock(id):
        return StockController.delete_one_stock(id)

    @app.route('/stocks/delete', methods=['DELETE'])
    def delete_all_stocks():
        return StockController.delete_all_stocks()