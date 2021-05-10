from flask import Flask, request, Response, jsonify
import json

from model.portfolio_model import PortfolioLineItem
from model.stock_model import Stock
from model.dividend_model import Dividend

from yahoo_fin import stock_info as si

class PortfolioService:
    
    def __init__(self):
        print("Portfolio Service Class Initialization")

    def get_portfolio(userId):
        """This method will get portfolio of a specific user"""
        print("<get_portfolio()>")
        print("userId: ", userId)
        
        match_userid = {
            "$match": {"user_id":userId, "transaction_type":"Buy"}
        }

        group_symbol = {
            "$group": 
            {"_id":"$symbol",
            "purchasedDate":{"$min":"$transaction_date"},
            "totalQuantity":{"$sum":"$quantity"},
            "avgPrice":{"$avg":"$price"},
            "totalBuyCost":{"$sum":{"$multiply":["$price","$quantity"]}}}  
        }

        sort_symbol_ascending = {
            "$sort":
            {"_id":1}
        }

        pipeline = [
            match_userid,
            group_symbol,
            sort_symbol_ascending,
        ]

        print("pipeline: ", pipeline)
        results = Stock.objects().aggregate(pipeline)
        retrievedStocks = list(results)
        portfolioLineItems = []
        
        for stock in retrievedStocks:
            print("\n -----------------------")
            print("stock: ", stock)

            match_div_userid = {
                "$match": {"user_id":userId}
            }

            group_div_symbol = {
                "$group": 
                {"_id":"$symbol",
                "totalDividend":{"$sum":"$total_dividend"}}  
            }

            sort_div_symbol_ascending = {
                "$sort":
                {"_id":1}
            }

            div_pipeline = [
                match_div_userid,
                group_div_symbol,
                sort_div_symbol_ascending,
            ]

            print("dividend pipeline: ", div_pipeline)
            div_results = Dividend.objects().aggregate(div_pipeline)
            retrievedDividends = list(div_results)      
            for div in retrievedDividends:
                print("\n -----------------------")
                print("dividend: ", div)

                curPrice = si.get_live_price(stock['_id'])
                currentPrice = round(curPrice,2)

                if (stock['_id'] == div['_id']):
                    portfolioLine = PortfolioLineItem(stock['_id'], stock['purchasedDate'], stock['totalQuantity'], stock['avgPrice'], stock['totalBuyCost'], div['totalDividend'], currentPrice)
                    portfolioLineItems.append(portfolioLine)
                    print("Added to PortfolioLineItems: ", portfolioLineItems)

        print("\n\n Final result sent back as PortfolioLineItems --> ", portfolioLineItems)
        
        return jsonify(portfolioLineItems)
        