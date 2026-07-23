
# Exercise 1: Book Class

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"'{self.title}' by {self.author} has {self.pages} pages.")

print("--- Exercise 1: Book Class ---")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Clean Code", "Robert C. Martin", 464)

book1.describe()
book2.describe()
print()



# Exercises 2

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price  
        self.quantity = quantity     
    def restock(self,n):    
        if n <= 0:
         print("Restock quanitity must be greater then 0.")
         return 
        self.quantity +=n
        print(f"Restocked {n} units. current stock of {self.name} : {self.quantity}")
        return
    def sell(self,n):
        if n <=0:
            print(f"sell quantity must be greater than 0.")
            return
        if self.quantity < n:
            print(f" insufficient stock to sell {n} units. only {self.quantity} found")
            return
        self.quantity -= n
        print(f"{n} units sold. now {self.quanity}:{self.name} remainig")
        
prod = Product("PC" ,50000,10)

prod.restock(5)
prod.sell(10)



        
# Exercise 3: Private attribute

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price      
        self.__quantity = quantity 

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        if n <= 0:
            print("Error: Restock quantity must be greater than 0.")
            return
        self.__quantity += n
        print(f"Restocked {n} units. Current stock of {self.name}: {self.__quantity}")

    def sell(self, n):
        if n <= 0:
            print("Error: Sell quantity must be greater than 0.")
            return
        if n > self.__quantity:
            print(f"Error: Insufficient stock to sell {n} units. Only {self.__quantity} available.")
            return
        self.__quantity -= n
        print(f"Sold {n} units. Remaining stock of {self.name}: {self.__quantity}")

prod = Product("Laptop", 45000, 10)
prod.restock(5)
prod.sell(3)
print(f"Final stock count via getter: {prod.quantity}")




#eXERCISE 4 - SETTER

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price       # in ETB
        self.__quantity = quantity  # Private variable

    @property
    def quantity(self):
        """Getter property to cleanly read the private quantity attribute."""
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        """Setter property that acts as a guard to refuse negative values."""
        if value < 0:
            print("Error: Quantity cannot go below zero.")
            return  
        self.__quantity = value

    def restock(self, n):
        if n <= 0:
            print("Error: Restock quantity must be greater than 0.")
            return
      
        self.quantity += n
        print(f"Restocked {n} units. Current stock of {self.name}: {self.quantity}")

    def sell(self, n):
        if n <= 0:
            print("Error: Sell quantity must be greater than 0.")
            return
        
        new_quantity = self.quantity - n
        if new_quantity < 0:
            print(f"Error: Insufficient stock to sell {n} units. Only {self.quantity} available.")
            return
            
        self.quantity = new_quantity
        print(f"Sold {n} units. Remaining stock of {self.name}: {self.quantity}")


prod = Product("Laptop", 45000, 10)
prod.sell(4)
prod.sell(12)
prod.quantity = -5
print(f"Final valid stock: {prod.quantity}")





   


# Exercise 5: Prove Independence


prod1 = Product("Coffee", 150, 50)
prod2 = Product("Tea", 80, 100)
prod3 = Product("Sugar", 120, 30)

# Display initial quantities
print(f"Before modification:")
print(f"  Prod 1 ({prod1.name}): {prod1.quantity}")
print(f"  Prod 2 ({prod2.name}): {prod2.quantity}")
print(f"  Prod 3 ({prod3.name}): {prod3.quantity}")

# Modify only the first product
print("\nModifying Prod 1 (selling 20 units)...")
prod1.sell(20)

# Show that the other two products remain unaffected
print("\nAfter modification:")
print(f"  Prod 1 ({prod1.name}): {prod1.quantity} (Changed)")
print(f"  Prod 2 ({prod2.name}): {prod2.quantity} (Unchanged)")
print(f"  Prod 3 ({prod3.name}): {prod3.quantity} (Unchanged)")