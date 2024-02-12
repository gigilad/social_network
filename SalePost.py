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
            print("Discount on ",self.owner.get_username(),"product! the new price is: ",self.price)
    def sold(self,password):
        if self.owner.get_password()==password:
           self.is_sold=True

       
        
            

