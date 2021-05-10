from app import app
from controller.login_controller import LoginController

class LoginRoute:

    def __init__(self):
        print("Login Route Class Initialization")

    @app.route('/login', methods=['POST'])
    def login():
        return LoginController.login()