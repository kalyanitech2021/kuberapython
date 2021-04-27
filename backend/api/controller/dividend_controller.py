from service.dividend_service import DividendService

class DividendController:
    
    def __init__(self):
        print("Dividend Controller Class Initialization")

    def add_dividend():
        return DividendService.add_dividend()

    def get_all_dividends(userId):
        return DividendService.get_all_dividends(userId)

    def get_one_dividend(id):
        return DividendService.get_one_dividend(id)

    def update_one_dividend(id):
        return DividendService.update_one_dividend(id)

    def delete_one_dividend(id):
        return DividendService.delete_one_dividend(id)

    def delete_all_dividends():
        return DividendService.delete_all_dividends()