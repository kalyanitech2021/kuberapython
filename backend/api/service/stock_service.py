from flask import Flask, request, Response, jsonify
import json

from model.stock_model import Stock

class StockService:
    
    def __init__(self):
        print("Stock Service Class Initialization")

    def add_stock():
        """This method will add a new stock"""
        print("<add_stock()>")
        body = request.get_json()
        stocks = Stock(**body).save()
        return jsonify(stocks)

    def get_all_stocks(userId):
        """This method will get all stocks for a specific user"""
        print("<get_all_stocks()>")
        print("userId: ", userId)
        stocks = Stock.objects(user_id=userId)
        return jsonify(json.loads(stocks.to_json()))

    def get_one_stock(id):
        """This method will get one stock for a specific id"""
        print("<get_one_stock()>")
        print("id: ", id)
        stocks = Stock.objects(id=id).first()
        return jsonify(json.loads(stocks.to_json()))

    def update_one_stock(id):
        """This method will update one stock for a specific id"""
        print("<update_one_stock()>")
        print("id: ", id)
        body = request.get_json()
        stocks = Stock.objects(id=id)
        stocks.update(**body)
        return jsonify(json.loads(stocks.to_json()))

    def delete_one_stock(id):
        """This method will delete one stock for a specific id"""
        print("<delete_one_stock()>")
        print("id: ", id)
        stocks = Stock.objects(id=id)
        stocks.delete()
        return jsonify(json.loads(stocks.to_json()))

    def delete_all_stocks():
        """This method will delete all stocks"""
        print("<delete_all_stocks()>")
        stocks = Stock.objects()
        stocks.delete()
        return jsonify(json.loads(stocks.to_json()))