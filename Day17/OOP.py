class User:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.followers=0
        self.following=0
    def follow(self,user):
        self.following+=1
        user.followers+=1
use_1=User('John',1)
user_2=User('Jack',2)
user_2.follow(use_1)
print(use_1.followers)
print(user_2.followers)
print(user_2.following)
print(use_1.following)