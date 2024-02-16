from Comment import Comment
from SomeObservers import LikeObserver,CommentObserver


class Post:
    def __init__(self, post_type, content, owner):
        self.type = post_type
        self.owner = owner
        self.content = content
        self.likes = []
        self.comments = []
        self.observers=[CommentObserver(),LikeObserver()]

    def like(self, user):
        if self.owner.get_username() != user.get_username():
            if user.is_online():
                for liked_user in self.likes:
                    if liked_user.get_username() == user.get_username():
                         print("this user already liked your post")
                         return
                self.likes.append(user)
                self.notify(self.owner,user,"like")
                self.owner.add_notification(f"{user.get_username()} liked your post")         

    def comment(self, user, comment_content):
        if self.owner.get_username() != user.get_username():
            if user.is_online():
                new_comment = Comment(user, comment_content)
                self.comments.append(new_comment)
                self.notify(self.owner,user,"comment",comment_content)
                self.owner.add_notification(f"{user.get_username()} commented on your post")


    def notify(self,post_owner,user,event_type,comment=None):
        for observer in self.observers:
            if event_type == "like" and isinstance(observer,LikeObserver):
                observer.update(post_owner,user)
            if event_type == "comment" and isinstance(observer,CommentObserver):
                observer.update(post_owner,user,comment)
    
    def get_content(self):
        return self.content

    def get_owner(self):
        return self.owner

    def get_likes(self):
        return self.likes

    def get_comments(self):
        return self.comments
    def get_owner(self):
        return self.owner