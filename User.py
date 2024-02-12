from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.online =True
        self.posts = []
        self.following_list = []

    def follow(self, user_to_follow):
        if self.online:
           
          if user_to_follow in self.following_list:
            raise ValueError(f"User {self.username} already follows {user_to_follow.username}")
          else:
            self.following_list.append(user_to_follow)
            print(f"{self.username} started following {user_to_follow.username}")

    def unfollow(self, user_to_unfollow):
        if self.online:
          if user_to_unfollow not in self.following_list:
            raise ValueError(f"User {self.username} is not following {user_to_unfollow.username}")
          else:
            self.following_list.remove(user_to_unfollow)
            print(f"{self.username} unfollowed {user_to_unfollow.username}")

    def publish_post(self, post_type, content, price=None, location=None):
        if self.online:
          if post_type == "Text":
            text_post = TextPost(post_type, content, self)
            self.posts.append(text_post)
            print(f"{self.username} published a post: {content}")
            return text_post
          elif post_type == "Image":
            image_post = ImagePost(post_type, content, self)
            self.posts.append(image_post)
            print(f"{self.username} posted a picture")
            return image_post
          elif post_type == "Sale":
            sale_post = SalePost(post_type, content, price, location, self)
            self.posts.append(sale_post)
            print(f"{self.username} posted a product for sale:")
            print(f"For sale!: {content}, price: {price}, pickup from: {location}")
            return sale_post
        else:
            raise ValueError("Invalid post type")

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_user_by_username(self, user_to_find):

        for i, user in enumerate(self.following_list):
            if user.get_username() == user_to_find.get_username():
                return i
        return -1
    def log_out(self):
        self.online=False
    def log_in(self):
        self.online=True
    def is_online(self):
       return self.is_online    
    def __str__(self):
       posts_count=len(self.posts)
       followers_count=len(self.following_list)
       return f"User name: {self.get_username()}, Number of posts: {posts_count}, Number of followers: {followers_count}"
       
        