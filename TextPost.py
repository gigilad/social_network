from Post import Post


class TextPost(Post):
    def __init__(self, post_type, content, owner):
        super().__init__(post_type, content, owner)
