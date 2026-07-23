class User():
    def __init__(self,name,email):
        self.name= name
        self.email=email

class userRepo():
    def save_to_db(self,user:User):
        print(f"save user : {user.name} to db") 

class Email():
     def send_welcome(self,user:User):
         print(f"sending welcome to {user.email}")

user=User("Abdi","abdi@gmail.com")

db=userRepo()
ema=Email()

db.save_to_db(user)
ema.send_welcome(user)
