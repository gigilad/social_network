from Post import Post


class SalePost(Post):
    def __init__(self, post_type, content, price, location, owner):
        super().__init__(post_type, content, owner)
        self.price = price
        self.location = location
        self.owner=owner
        self.is_sold=False
    def discount(self,amount,password):
        if self.is_sold is False:
          if self.owner.get_password()==password:
             self.price = self.price - (self.price*(amount/100))
             print(f"Discount on {self.owner.get_username()} product! the new price is: {self.price}")
    def sold(self,password):
        if self.owner.get_password() == password:
           self.is_sold=True
           print(f"{self.owner.get_username()}'s product is sold")
    def __str__(self):
       available ="Sold!" if self.is_sold else "available"
       result = f"{self.get_owner().get_username()} posted a product for sale:\n"
       return result +f"{available} {self.content}, price: {self.price}, pickup from: {self.location}"
       
       
        
            

