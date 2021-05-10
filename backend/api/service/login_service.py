from flask import Flask, request, Response, jsonify
import json
from flask_login import (current_user, LoginManager, login_user, logout_user, login_required)
from model.users_model import User

class LoginService:
    
    def __init__(self):
        print("Login Service Class Initialization")

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.user_loader    
    def load_user(user_id):
        try:
            return User.objects(id=user_id).first()
        except:
            return None

    def login():
        """This method will authenticate if user is a valid user"""
        print("<login()>")
        info = json.loads(request.data)
        user_id = info.get('user_id')
        password = info.get('password')
        user = User.objects(user_id=user_id,
                        password=password).first()
        if user:
            login_user(user)
            return jsonify(user.to_json())
        else:
            return jsonify({"status": 401, "reason": "Username or Password Error"})