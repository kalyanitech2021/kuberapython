from service.stock_service import StockService

class StockController:
    
    def __init__(self):
        print("Stock Controller Class Initialization")

    def add_stock():
        return StockService.add_stock()

    def get_all_stocks(userId):
        return StockService.get_all_stocks(userId)

    def get_one_stock(id):
        return StockService.get_one_stock(id)

    def update_one_stock(id):
        return StockService.update_one_stock(id)

    def delete_one_stock(id):
        return StockService.delete_one_stock(id)

    def delete_all_stocks():
        return StockService.delete_all_stocks()