class Observer:
    def update(self, *args, **kwargs):
        pass
    
class LikeObserver(Observer):
    def update(self,post_owner,user):
         if post_owner.get_username() != user.get_username():
            print(f"notification to {post_owner.get_username()}: {user.get_username()} liked your post")

class CommentObserver(Observer):
    def update(self,post_owner,user,comment):
        if post_owner.get_username() != user.get_username():
           print(f"notification to {post_owner.get_username()}: {user.get_username()} commented on your post: {comment}")

class PostObserver(Observer):
    def update(self,post):
        for user in post.owner.get_followers_list():
            user.add_notification(f"{post.get_owner().get_username()} has a new post")
            
            
