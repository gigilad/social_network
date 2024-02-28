from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost

class PostFactory:
    @staticmethod
    def createPost(post_type, content,owner, price=None, location=None,):
        post = None
        if post_type == "Text":
            post = TextPost(post_type,content, owner)
            print(f"{post.owner.get_username()} published a post:\n\"{content}\"\n")
        elif post_type == "Image":
            post = ImagePost(post_type, content, owner)
            print(f"{post.owner.get_username()} posted a picture\n")
        elif post_type == "Sale":
            post = SalePost(post_type, content, price, location, owner)
            print(f"{post.owner.get_username()} posted a product for sale:")
            print(f"For sale! {content}, price: {price}, pickup from: {location}\n")
        return post