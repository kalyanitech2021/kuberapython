from flask import Flask, request, Response, jsonify
import json

from model.dividend_model import Dividend

class DividendService:
    
    def __init__(self):
        print("Dividend Service Class Initialization")

    def add_dividend():
        """This method will add a new dividend"""
        print("<add_dividend()>")
        body = request.get_json()
        total_dividend = float(body['quantity']) * float(body['div_per_share'])
        body['total_dividend'] = total_dividend
        dividends = Dividend(**body).save()
        return jsonify(dividends)

    def get_all_dividends(userId):
        """This method will get all dividends for a specific user"""
        print("<get_all_dividends()>")
        print("userId: ", userId)
        dividends = Dividend.objects(user_id=userId)
        return jsonify(json.loads(dividends.to_json()))

    def get_one_dividend(id):
        """This method will get one dividend for a specific id"""
        print("<get_one_dividend()>")
        print("id: ", id)
        dividends = Dividend.objects(id=id).first()
        return jsonify(json.loads(dividends.to_json()))

    def update_one_dividend(id):
        """This method will update one dividend for a specific id"""
        print("<update_one_dividend()>")
        print("id: ", id)
        body = request.get_json()
        dividends = Dividend.objects(id=id)
        dividends.update(**body)
        return jsonify(json.loads(dividends.to_json()))

    def delete_one_dividend(id):
        """This method will delete one dividend for a specific id"""
        print("<delete_one_dividend()>")
        print("id: ", id)
        dividends = Dividend.objects(id=id)
        dividends.delete()
        return jsonify(json.loads(dividends.to_json()))

    def delete_all_dividends():
        """This method will delete all dividends"""
        print("<delete_all_dividends()>")
        dividends = Dividend.objects()
        dividends.delete()
        return jsonify(json.loads(dividends.to_json()))