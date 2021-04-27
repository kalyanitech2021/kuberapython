from service.users_service import UsersService

class UsersController:
    
    def __init__(self):
        print("Users Controller Class Initialization")

    def add_user():
        return UsersService.add_user()