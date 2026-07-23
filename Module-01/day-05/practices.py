from abc import ABC, abstractmethod
#exercise 1
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self)
        print(f"vehicle: {self.make} {self.model}")
        

class Car(Vehicle):
    pass

    

class Truck(Vehicle):
      pass



#exercise2
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self)
        print(f"vehicle: {self.make} {self.model}")
        

class Car(Vehicle):
    pass

    

class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity


#exercise 3
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self)
        print(f"vehicle: {self.make} {self.model}")
        

class Car(Vehicle):
    pass

    

class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity
    def describe(self):
        print(f"Vehicle: {self.make} {self.model}, Capacity: {self.capacity}")


#exercise 4
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self)
        print(f"vehicle: {self.make} {self.model}")
        

class Car(Vehicle):
    pass

    

class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity
    def describe(self):
        print(f"Vehicle: {self.make} {self.model}, Capacity: {self.capacity}")

vehicles = [
    Vehicle("Toyota", "Corolla"),
    Car("Honda", "Civic"),
    Truck("Volvo", "FH16", "20 tons")
]

for vehicle in vehicles:
    vehicle.describe()




#exercise 5
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self)
        print(f"vehicle: {self.make} {self.model}")
        
    @abstractmethod
    def wheels(self):
        pass

class Car(Vehicle):
    def wheels(self):
        return 4

    

class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity
    def describe(self):
        print(f"Vehicle: {self.make} {self.model}, Capacity: {self.capacity}")
    def wheels(self):
        return 18
    

vehicles = [
    Vehicle("Toyota", "Corolla"),
    Car("Honda", "Civic"),
    Truck("Volvo", "FH16", "20 tons")
]

for vehicle in vehicles:
    vehicle.describe()
