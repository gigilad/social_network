from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost
from SomeObservers import PostObserver


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.online =True
        self.posts = []
        self.following_list = []
        self.followers_list = []
        self.notifications = []
        self.post_observer =PostObserver()

    def follow(self, user_to_follow):
        if self.online:
          if user_to_follow in self.following_list:
            raise ValueError(f"User {self.username} already follows {user_to_follow.username}")
          else:
            self.following_list.append(user_to_follow)
            user_to_follow.add_follower(self)
            print(f"{self.username} started following {user_to_follow.username}")

    def unfollow(self, user_to_unfollow):
        if self.online:
          if user_to_unfollow not in self.following_list:
            raise ValueError(f"User {self.username} is not following {user_to_unfollow.username}")
          else:
            self.following_list.remove(user_to_unfollow)
            user_to_unfollow.remove_user_from_follower_list(self)
            print(f"{self.username} unfollowed {user_to_unfollow.username}")
       
    def publish_post(self, post_type, content, price=None, location=None):
        if self.online:
          if post_type == "Text":
            text_post = TextPost(post_type,content, self)
            self.posts.append(text_post)
            print(f"{self.username} published a post:\n\"{content}\"\n")
            self.post_observer.update(text_post)
            return text_post
          elif post_type == "Image":
            image_post = ImagePost(post_type, content, self)
            self.posts.append(image_post)
            print(f"{self.username} posted a picture\n")
            self.post_observer.update(image_post)
            return image_post
          elif post_type == "Sale":
            sale_post = SalePost(post_type, content, price, location, self)
            self.posts.append(sale_post)
            print(f"{self.username} posted a product for sale:")
            print(f"For sale! {content}, price: {price}, pickup from: {location}\n")
            self.post_observer.update(sale_post)    
            return sale_post
        else:
            raise ValueError("Invalid post type")

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def log_out(self):
        self.online=False
    def log_in(self):
        self.online=True
    def is_online(self):
       return self.is_online    
    def __str__(self):
       posts_count=len(self.posts)
       followers_count=len(self.followers_list)
       return f"User name: {self.get_username()}, Number of posts: {posts_count}, Number of followers: {followers_count}"
    def add_notification(self,notification):
       self.notifications.append(notification)

    def print_notifications(self):
         print(f"{self.username}'s notifications:")
         for notification in self.notifications:
            print(notification)
    def get_following_list(self):
       return self.following_list   
    def add_follower(self,follower):
       self.followers_list.append(follower)    
    def get_followers_list(self):
       return self.followers_list   
    def remove_user_from_follower_list(self,user):
       self.followers_list.remove(user)