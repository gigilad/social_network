
from UserFactory import UserFactory


class SocialNetwork:
    instance = None

    def __init__(self, name):
        self.social_name = name
        self.users = []
        print("The social network", name, "was created!")

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls("twitter")
        return cls.instance

    def sign_up(self, user_name, password):
        new_user = UserFactory.create_user(user_name, password, self.users)
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
            
            