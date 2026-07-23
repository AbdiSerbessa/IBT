# class Account:
#     def __init__(self, owner,balance):
#         self.owner = owner
#         self.__balance = balance
#     def deposit(self,amount):
#         if amount <= 0:
#             print("you can't deposit this amount")
#             return
#         self.__balance += amount
#     def statement(self):
#         print(f"{self.owner} : {self.__balance}")
#         return
    
#     def withdraw(self,amount):
#         if amount > self.__balance:
#             print("insufficient fund")
#             return
#         self.__balance -= amount
# abdi = Account("Abdi Serbessa", 10000)
# abdi.deposit(500)
# abdi.withdraw(1000)
# abdi.statement()


# class Account:
#     def __init__(self, balance):
#       self.__balance = balance # private
#     def withdraw(self, amount):
#         if amount > self.__balance:
#           print("Insufficient funds")
#           return
#         self.__balance -= amount
#     def get_balance(self):
#        return self.__balance
# abdi = Account(2000)


# print(f"your balance is {abdi.get_balance()}")        
# abdi.withdraw(4000)


# class Account:
#     def __init__(self, balance):
#         self.__balance = balance
#     @property
#     def balance(self): # getter
#       return self.__balance
#     @balance.setter
#     def balance(self, value): # setter with validation
#         if value < 0:
#          raise ValueError("No negative balance")
#         self.__balance = value
# a = Account(1500)
# #a.balance = 1500 #(runs the getter)

# a.balance = 2000 # ok (runs the setter)
# a.balance = -5 # ValueError
# print(f"{a.balance}")


# class Book:
#     def __init__(self, title, author,page):
#         self.title = title
#         self.author = author
#         self.page = page

#     def describe(self):
#         print(f" The book called '{self.title}' was written by {self.author} has {self.page} pages")

# book1 = Book("Volcano","James.j", 300)
# book2 = Book("Nature","Abdii" , 400)

# book1.describe()
# book2.describe()



# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price  
#         self.quantity = quantity     
#     def restock(self,n):    
#         if n <= 0:
#          print("Restock quanitity must be greater then 0.")
#          return 
#         self.quantity +=n
#         print(f"Restocked {n} units. current stock of {self.name} : {self.quantity}")
#         return
#     def sell(self,n):
#         if n <=0:
#             print(f"sell quantity must be greater than 0.")
#             return
#         if self.quantity < n:
#             print(f" insufficient stock to sell {n} units. only {self.quantity} found")
#             return
#         self.quantity -= n
#         print(f"{n} units sold. now {self.quantity}:{self.name} remainig")
        
# prod = Product("PC" ,50000,10)

# prod.restock(5)
# prod.sell(2)        


# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price       # in ETB
#         self.__quantity = quantity  # Made private

#     @property
#     def quantity(self):
#         return self.__quantity

#     def restock(self, n):
#         if n <= 0:
#             print("Error: Restock quantity must be greater than 0.")
#             return
#         self.__quantity += n
#         print(f"Restocked {n} units. Current stock of {self.name}: {self.__quantity}")

#     def sell(self, n):
#         if n <= 0:
#             print("Error: Sell quantity must be greater than 0.")
#             return
#         if n > self.__quantity:
#             print(f"Error: Insufficient stock to sell {n} units. Only {self.__quantity} available.")
#             return
#         self.__quantity -= n
#         print(f"Sold {n} units. Remaining stock of {self.name}: {self.__quantity}")

# prod = Product("Laptop", 45000, 10)
# prod.restock(5)
# prod.sell(3)
# print(f"Final stock count via getter: {prod.quantity}")


# class Account:
#     def __init__(self,owner,account_number,balance):
#         self.owner = owner
#         self.account_number = account_number
#         self.__balance = balance

#     @property
#     def balance(self):
#         return self.__balance
    
#     def deposit(self,amount):
#         if amount <=0:
#             print("you can't deposit zero and below zero")
#             return
#         self.__balance += amount
#         print("deposited successfully")
#         return
#     def withdraw(self,amount):
#         if amount <= 0:
#             print("you can't withdraw this amount")
#             return
#         if self.__balance < amount:
#             print("INSUFFICIENT FUND")
#             return
#         self.__balance -= amount
#         print(f"withdrawn successfully")
#         return
# acc1 = Account("Abdi serbessa",10002180,100000)
# acc2 = Account("Nohi Tesfaye",10006502,200000)

# acc1.deposit(1000)
# acc2.deposit(1000)
# acc1.withdraw(0)

# class Account:
#     def __init__(self,owner,balance=0):
#         self.owner = owner
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance +=amount

# class SavingAccount(Account):
#     def __int__(self,owner,balance=0,rate = 0.015):
#         super().__init__(owner,balance)
#         self.rate = rate
#     def add_interest(self):
#         self.deposit(self.balance*self.rate)
# sa = SavingAccount("Abdi Serbessa",1000)

# sa.deposit(500)
# print(sa.balance)
        

# class Account:
#     def __init__(self,owner,balance=0):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance +=amount

#     def withdraw(self,amount):
#         self.balance -=amount
#     def statement(self):
#         print(f"{self.owner} : {self.balance}")
#         return
# class SavingAccount(Account):
#       pass

# sa = SavingAccount("Abdi Serbessa",1000)

# sa.statement()

# class Account:
#     def __init__(self,owner,balance=0):
#         self.owner=owner
#         self.balance=balance
#     def withdraw(self,amount):
#         self.balance -=amount
#         print(f"withdarwn {amount} ETB from {self.owner } account")
#         return
# class SavingAccount(Account):
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             print(f"{self.owner} : withdrawn {amount}   ETB")
#             return
#         super().withdraw(amount)
# basic = Account("Serbessa Irko", 10000)

# sa = SavingAccount("Abdi Serbessa",1000)

# basic.withdraw(1000)
# sa.withdraw (500)




### ENCAPSULATION INHERITANCE, OVERRIDING , POLYMORPHISM CONCEPST###

# class Account:
#     def __init__(self,owner,balance=0):
#         self.owner= owner
#         self.balance=balance

#     def withdraw(self,amount):
#         self.balance -=amount
#         print(f"withdraw from {self.owner} : {self.balance} ETB")
        
# class SavingAccount(Account):
#     def withdraw(self, amount):
#         if self.balance < amount :
#             print(f"insufficient fund. you have only {self.balance} ETB")
#             return
#         super().withdraw(amount)
# class CurrentAccount(Account):
#     def __init__(self,owner,balance=0,overdraft_limit=2000):
#         super().__init__(owner,balance)
#         self.overdraft_limit=overdraft_limit
#     def withdraw(self, amount):
#         if amount > (self.balance+self.overdraft_limit):
#             print(f"declined: {amount} exceeded the the overdrft_limit {self.overdraft_limit} ETB ")
#             return
#         self.balance -=amount
#         print(f"withdrawn successfully {amount} ETB overdraft used by {self.owner}")


# accounts = [
#     SavingAccount("Abdi Serbessa" , 5000),
#     CurrentAccount("Nohi Tesfaye",6000,2000)
# ]
# for acc in accounts:
#  acc.withdraw(1000)
        




###### ABSTRACTION CONCEPT######

# from abc import ABC , abstractmethod
# class Account(ABC):
#     def __init__(self,owner,balance=0):
#         self.owner = owner
#         self.balance= balance

#     @abstractmethod
#     def apply_monthly_fees(self):
#         """any implemmentation here"""
#         pass

# class SavingAccount(Account):
#     def apply_monthly_fees(self):
#         print(f"this is saving accont of class and no fees applied to {self.owner} this month")

# class CheckingAccount(Account):
#     def apply_monthly_fees(self):
#         self.balance -= 150
#         print(f" Monthly fee applied to {self.owner} Account this month")

# sa = SavingAccount("Abdi Serbessa",5000)
# ca = CheckingAccount("Feyera Serbessa",10000)

# sa.apply_monthly_fees()
# ca.apply_monthly_fees()



      ###exercise1  

# class vehicle:
#     def __init__(self,make,model):
#         self.make=make
#         self.model=model
#     def describe(self):
#          return f"vehicle was made by {self.make} and it is a {self.model} model" 


# class Car(vehicle):
#     def __init__(self, make, model,car_doors):
#         super().__init__(make, model)
#         self.car_doors=car_doors
#     def describe(self):
#         return f"Car: {self.make} {self.model}"
        
        
        
# class Truck(vehicle):
#     def __init__(self, make, model,capacity):
#         super().__init__( make,model)
#         self.capacity = capacity
#     def describe(self):
#         return f"Truck: {self.make} {self.model}"

# my_car=Car("ABDI",2026,2)
# my_truck=Truck("nohi" , 2026,2)


# station = [
#     my_car,my_truck
# ]       

# for vehicle in station:
#    print( vehicle.describe())



# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     def __init__(self,make,model):
#         self.make=make
#         self.model=model
#     def describe(self):
#         return f"{self.make} {self.model}"
  
#     @abstractmethod
#     def wheels(self):
#         pass

# class Car(vehicle):
#     def __init__(self, make, model):
#         super().__init__(make, model)
#     # def describe(self):
#     #     return f"{self.make} {self.model}"
#     def wheels(self):
#         return 1
    
# class Truck(vehicle):
#     def __init__(self, make, model,capacity):
#         super().__init__(make, model)
#         self.capacity=capacity
#     # def describe(self):
#     #     return f"{self.make} {self.model} {self.capacity}"
#     def wheels(self):
#         return 2

# my_car = Car("Abdi",2025)
# my_track = Truck("nohi",2026,10)

# parking=[my_car,my_track]

# for vehicle in parking:
#     print(f"{vehicle.describe()} has {vehicle.wheels()}")






# #########################################################################
# # account.py day04

# class Account:
#     def __init__(self, owner: str, account_number: str, initial_balance: float = 0.0):
#         self.owner = owner
#         self.account_number = account_number
#         if initial_balance < 0:
#             raise ValueError("Initial balance cannot be negative.")
#         self.__balance = initial_balance
#     @property
#     def balance(self) -> float:
#         return self.__balance   
    
#     def deposit(self, amount: float) -> None:
#         if amount <= 0:
#             print(f"❌ Deposit Rejected: Deposit amount must be positive. Attempted: {amount:.2f} ETB.")
#             return  
#         self.__balance += amount
#         print(f"✅ Deposit Successful: Added {amount:.2f} ETB. New Balance: {self.__balance:.2f} ETB.")

    

#     def withdraw(self, amount: float) -> bool:
#         if amount <= 0:
#             print(f"❌ Withdrawal Rejected: Amount must be positive. Attempted: {amount:.2f} ETB.")
#             return False  
#         if amount > self.__balance:
#            print(f"❌ Overdraft Rejected: Insufficient funds. Requested {amount:.2f} ETB, but current balance is {self.__balance:.2f} ETB.")
#            return False  
            
#         print(f"💸 Withdrawal Successful: Withdrew {amount:.2f} ETB. Remaining Balance: {self.__balance:.2f} ETB.")
#         return True

# account_1 = Account(owner="Abdisa", account_number="ACC-1001", initial_balance=500.0)
# account_2 = Account(owner="Sifan", account_number="ACC-1002", initial_balance=250.0)    


# account_1.deposit(200.0)         
# account_1.withdraw(150.0)        
# account_1.deposit(-50.0)

# account_2.withdraw(500.0)        
# account_2.deposit(100.0)         
# account_2.withdraw(300.0)

# print(f"Final Balance ({account_1.owner}): {account_1.balance:.2f} ETB")
# print(f"Final Balance ({account_2.owner}): {account_2.balance:.2f} ETB")


# day05/accounts.py

# class Account:
#     """
#     Base class for all account types in Addis Bank.
#     """
#     def __init__(self, owner: str, account_number: str, initial_balance: float = 0.0):
#         self.owner = owner
#         self.account_number = account_number
        
#         if initial_balance < 0:
#             raise ValueError("Initial balance cannot be negative.")
#         # Step 1: Protected balance attribute (_balance) for inheritance
#         self._balance = initial_balance

#     @property
#     def balance(self) -> float:
#         """Read-only property to view the current balance."""
#         return self._balance

#     def deposit(self, amount: float) -> None:
#         """Deposits a positive amount into the account."""
#         if amount <= 0:
#             print(f"❌ Deposit Rejected: Amount must be positive. Attempted: {amount:.2f} ETB.")
#             return
#         self._balance += amount
#         print(f"✅ Deposit Successful: Added {amount:.2f} ETB. New Balance: {self._balance:.2f} ETB.")

#     def withdraw(self, amount: float) -> bool:
#         """Base withdrawal validation (no overdraft)."""
#         if amount <= 0:
#             print(f"❌ Withdrawal Rejected: Amount must be positive. Attempted: {amount:.2f} ETB.")
#             return False
            
#         if amount > self._balance:
#             print(f"❌ Overdraft Rejected: Insufficient funds. Balance: {self._balance:.2f} ETB.")
#             return False
            
#         self._balance -= amount
#         print(f"💸 Withdrawal Successful: Withdrew {amount:.2f} ETB. Remaining: {self._balance:.2f} ETB.")
#         return True

   
# print(f"ACCOUNT | Owner: {self.owner} | No: {self.account_number} | Balance: {self._balance:.2f} ETB")













# day06/bank.py
class AlertService:
    def success(self, message):
        print(f"✔ {message}")

    def error(self, message):
        print(f"❌ {message}")

    def warning(self, message):
        print(f"⚠ {message}")

    def info(self, message):
        print(f"ℹ {message}")
        
alert_service = AlertService()  

class SMSAlert:
    def update(self, account, event_type, message):
        print(f"📱 [SMS Alert -> {account.owner}]: [{event_type.upper()}] {message}")

class Account:
    def __init__(self, owner, account_number, initial_balance=0.0):
        self.owner = owner.strip().title()
        self.account_number = str(account_number).strip()
        self._subscribers = []
        if initial_balance < 0:
            alert_service.warning(f"Initial balance cannot be negative. Setting balance to 0.0 ETB for {self.owner}.")
            self.__balance = 0.0
        else:
            self.__balance = float(initial_balance)
    def subscribe(self, observer):
        if observer not in self._subscribers:
            self._subscribers.append(observer)

    def unsubscribe(self, observer):
        if observer in self._subscribers:
            self._subscribers.remove(observer)

    def _notify(self, event_type, message):
        for sub in self._subscribers:
            sub.update(self, event_type, message)


    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            alert_service.error(f"Transaction Failed [{self.owner}]: Cannot deposit a negative or zero amount ({amount} ETB).")
            return False

        self.__balance += amount
        msg = f"Deposited {amount:.2f} ETB. New Balance: {self.__balance:.2f} ETB."
        alert_service.success(f"Deposit Successful [{self.owner}]: {msg}")
        
        
        self._notify("deposit", msg)
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            alert_service.error(f"Transaction Failed [{self.owner}]: Cannot withdraw a negative or zero amount ({amount} ETB).")
            return False

        if amount > self.__balance:
            alert_service.error(f"Transaction Failed [{self.owner}]: Overdraft rejected! Tried to withdraw {amount:.2f} ETB, but only {self.__balance:.2f} ETB is available.")
            return False

        msg = f"Withdrew {amount:.2f} ETB. New Balance: {self.__balance:.2f} ETB."
        alert_service.success(f"Withdrawal Successful [{self.owner}]: {msg}")
        
        self._notify("withdrawal", msg)
        return True
    def statement(self):
        alert_service.info(f"[Standard Account] No: {self.account_number} | Owner: {self.owner} | Balance: {self.balance:.2f} ETB")


class SavingsAccount(Account):
    def __init__(self, owner, account_number, initial_balance=0.0, rate=0.05):
        super().__init__(owner, account_number, initial_balance)
        self.rate = float(rate)

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)
        alert_service.info(f"Interest Added [{self.owner}]: Earned {interest:.2f} ETB at {self.rate * 100:.1f}% rate.")

    def statement(self):
        alert_service.info(f"[Savings Account] No: {self.account_number} | Owner: {self.owner} | Balance: {self.balance:.2f} ETB | Interest Rate: {self.rate * 100:.1f}%")


class CurrentAccount(Account):
    def __init__(self, owner, account_number, initial_balance=0.0, overdraft_limit=1000.0):
        super().__init__(owner, account_number, initial_balance)
        self.overdraft_limit = float(overdraft_limit)

    def withdraw(self, amount):
        if amount <= 0:
            alert_service.error(f"Transaction Failed [{self.owner}]: Cannot withdraw a negative or zero amount ({amount} ETB).")
            return False

        max_allowed = self.balance + self.overdraft_limit
        if amount > max_allowed:
            alert_service.error(f"Transaction Failed [{self.owner}]: Exceeds overdraft limit! Maximum allowed withdrawal: {max_allowed:.2f} ETB.")
            return False

        if amount <= self.balance:
            return super().withdraw(amount)
        else:
            self._Account__balance -= amount
            msg = f"Withdrew {amount:.2f} ETB (Overdraft). New Balance: {self.balance:.2f} ETB."
            alert_service.warning(f"Overdraft Used [{self.owner}]: {msg}")

            self._notify("overdraft_withdrawal", msg)
            return True

    def statement(self):
        alert_service.info(f"[Current Account] No: {self.account_number} | Owner: {self.owner} | Balance: {self.balance:.2f} ETB | Overdraft Limit: {self.overdraft_limit:.2f} ETB")

class AccountFactory:
    def create(self, kind, owner, account_number, initial_balance=0.0, **kwargs):
        kind_clean = str(kind).strip().lower()

        if kind_clean in ["savings", "saving"]:
            rate = kwargs.get("rate", 0.05)
            return SavingsAccount(
                owner=owner, 
                account_number=account_number, 
                initial_balance=initial_balance, 
                rate=rate
            )

        elif kind_clean in ["current", "checking"]:
            overdraft_limit = kwargs.get("overdraft_limit", 1000.0)
            return CurrentAccount(
                owner=owner, 
                account_number=account_number, 
                initial_balance=initial_balance, 
                overdraft_limit=overdraft_limit
            )

        elif kind_clean in ["standard", "base", "account"]:
            return Account(
                owner=owner, 
                account_number=account_number, 
                initial_balance=initial_balance
            )

        else:
            alert_service.error(f"AccountFactory Error: Unknown account type '{kind}'.")
            return None
        
factory = AccountFactory()
sms_alert = SMSAlert()

if __name__ == "__main__":
  
    factory = AccountFactory()
    sms_alert = SMSAlert()

    accounts = [
        factory.create("standard", owner="Abdi", account_number="100023456", initial_balance=500.0),
        factory.create("savings", owner="Sifan", account_number="200098765", initial_balance=1000.0, rate=0.07),
        factory.create("current", owner="Abdi", account_number="300054321", initial_balance=200.0, overdraft_limit=500.0)
    ]

    for acc in accounts:
        if acc:
            acc.subscribe(sms_alert)

    
    accounts[1].add_interest()     
    accounts[2].withdraw(400.0)   


    for acc in accounts:
        if acc:
            acc.statement()

