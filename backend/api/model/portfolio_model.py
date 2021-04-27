import json

class PortfolioLineItem(dict):
    def __init__(self, p_symbol, p_date, p_ttlQty, p_avgPrice, p_ttlBuyCost, p_ttlDiv, p_currPrice):
        dict.__init__(
            self,
            symbol=p_symbol, 
            purchasedDate=p_date, 
            totalQuantity=p_ttlQty, 
            avgPrice=p_avgPrice, 
            totalBuyCost=p_ttlBuyCost,
            totalDividend=p_ttlDiv,
            currentPrice=p_currPrice
            )