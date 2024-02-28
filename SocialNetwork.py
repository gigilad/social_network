
from User import User
class SocialNetwork:
    _instance = None

    def __init__(self, name):
        if SocialNetwork._instance is None:
            self.social_name = name
            self.users = []
            print("The social network", name, "was created!")
            SocialNetwork._instance = self
        else:
            print(f"Instance for {name} already exists.") 
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise Exception("No instance of SocialNetwork exists. Use the constructor to create an instance.")
        return cls._instance

    def create_user(self,username, password):
        if len(password) < 4 or len(password) > 8:
            raise ValueError("Password needs to be between 4 to 8 characters")
        if len(username) == 0:
            raise ValueError("Username cannot be empty")
        if self.is_username_exists(username):
            raise ValueError("User already exists")
        return User(username, password)
    
    def is_username_exists(self, username):
        for user in self.users:
            if user.get_username() == username:
                return True
        return False   
    def sign_up(self, user_name, password):
        new_user = self.create_user(user_name, password)
        self.users.append(new_user)
        return new_user
    
    def log_out(self,username):
        for user in self.users:
         if user.get_username() == username:
            user.log_out
            print(user.get_username(),"disconnected")
            return
         
    def log_in(self,user_name,password):
        for user in self.users:
            if user.get_username() == user_name and user.get_password() == password:
               user.log_in()
               print(user.get_username(),"connected")
               return
        print(f"Username or Password wrong")   

    def __str__(self):
       result = f"{self.social_name} social network:\n"
       for user in self.users:
         result += str(user) + "\n"
       return result
            
            