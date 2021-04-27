from flask import Flask, request, Response, jsonify
import json
from model.users_model import User
from mongoengine.errors import NotUniqueError

class UsersService():    
    def __init__(self):
        print("Users Service Class Initialization")

    def add_user():
        """This method will add a new user"""
        print("<add_user()>")
        try:
            body = request.get_json()
            users = User(**body).save()
            return jsonify(users)
        except NotUniqueError:
            print("Error: Username already exists. Please enter a different username.")
        else:
            print("User registered successfully")