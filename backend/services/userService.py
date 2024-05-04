from models.createModels import User

class UserService:
    def __init__(self) -> None:
        pass

    def createUser(self, name):
        print(name)
        user_id = User.create(name=name)
        print('User saved successfully')
        return user_id

    def findUser(self, name):
        try:
            user_id = User.get(User.name == name)
        except: 
            user_id = self.createUser(name)
        return user_id
    
    def getAllUser(self):
        return User.select()