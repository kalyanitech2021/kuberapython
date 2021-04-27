from app import app
from controller.portfolio_controller import PortfolioController

class PortfolioRoute:

    def __init__(self):
        print("Portfolio Route Class Initialization")

    @app.route('/portfolio/<userId>')
    def get_portfolio(userId):
        return PortfolioController.get_portfolio(userId)

