from app import app
from controller.users_controller import UsersController

class UsersRoute:

    def __init__(self):
        print("Users Route Class Initialization")

    @app.route('/users', methods=['POST'])
    def add_user():
        return UsersController.add_user()