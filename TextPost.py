from Post import Post


class TextPost(Post):
    def __init__(self, post_type, content, owner):
        super().__init__(post_type, content, owner)
    def __str__(self):
        return f"{self.get_owner().get_username()} published a post:\n\"{self.content}\""
            
