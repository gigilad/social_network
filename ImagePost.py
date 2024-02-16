from Post import Post
# import matplotlib.pyplot as plt
# from matplotlib.image import imread


class ImagePost(Post):
    def __init__(self, post_type, content, owner):
        super().__init__(post_type, content, owner)
    def __str__(self):
        return f"{self.owner.get_username()} posted a picture"    

    # def display(self):
    #     image_data= imread(self.content)
    #     plt.imshow(image_data)
    #     plt.axis('off')
    #     plt.show()
        