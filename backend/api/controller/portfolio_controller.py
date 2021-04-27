from service.portfolio_service import PortfolioService

class PortfolioController:
    
    def __init__(self):
        print("Portfolio Controller Class Initialization")

    def get_portfolio(userId):
        return PortfolioService.get_portfolio(userId)