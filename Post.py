from Comment import Comment


class Post:
    def __init__(self, post_type, content, owner):
        self.type = post_type
        self.owner = owner
        self.content = content
        self.likes = []
        self.comments = []

    def like(self, user):
        for liked_user in self.likes:
            if liked_user.get_username() == user.get_username():
                return
        self.likes.append(user)
        print("Notification to " + self.owner.get_username() + ": " + user.get_username() + " liked your post")

    def comment(self, user, comment_content):
        new_comment = Comment(user, comment_content)
        self.comments.append(new_comment)
        print("Notification to " + self.owner.get_username() + ": " + user.get_username() +
              " commented on your post " + comment_content)

    def get_content(self):
        return self.content

    def get_owner(self):
        return self.owner

    def get_likes(self):
        return self.likes

    def get_comments(self):
        return self.comments