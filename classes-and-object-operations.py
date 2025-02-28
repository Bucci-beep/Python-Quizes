# Scenario: Car dealership inventory management system
# Task-1. You are tasked with creating a Python program to represent vehicles using a class. Each car should have attributes for maximum speed and mileage.

class Vehicle(object):
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed;
        self. mileage = mileage;
        
# Task-2. Update the class with the default color for all vehicles," white".

class Vehicle(object):
    def __init__(self, max_speed, mileage, color = "white"):
        self.max_speed = max_speed;
        self. mileage = mileage;
        self.color = color;
        
# Task-3. Additionally, you need to create methods in the Vehicle class to assign seating capacity to a vehicle.

class Vehicle(object):
    def __init__(self, max_speed, mileage, color = "white"):
        self.max_speed = max_speed;
        self. mileage = mileage;
        self.color = color;
    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity;

# Task-4. Create a method to display all the properties of an object of the class.

class Vehicle(object):
    def __init__(self, max_speed, mileage, color = "white"):
        self.max_speed = max_speed
        self. mileage = mileage
        self.color = color
        
    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity
        
    def vehicle_info(self):
        print("Vehicle Properties:")
        print("max_speed:", self.max_speed)
        print("mileage:", self.mileage)
        print("color:", self.color)
        print("seating_capacity:", self.seating_capacity)     

# Task-5. Additionally, you need to create two objects of the Vehicle class object that should have a max speed of 200kph and mileage of 50000kmpl with five seating capacities, and another car object should have a max speed of 180kph and 75000kmpl with four seating capacities.

class Vehicle(object):
    def __init__(self, max_speed, mileage, color="white"):
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color
        
    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity
        
    def vehicle_info(self):
        print("Vehicle Properties:")
        print("max_speed:", self.max_speed)
        print("mileage:", self.mileage)
        print("color:", self.color)
        print("seating_capacity:", self.seating_capacity)    
    
# Create objects with a valid color (or let it default to "white")
car1 = Vehicle("200kph", "50000kmpl")
car2 = Vehicle("180kph", "75000")

# Set seating capacity separately
car1.assign_seating_capacity(5)
car2.assign_seating_capacity(4)

# Task-6. Display all the properties of both objects.

cars = [car1, car2]
for car in cars:
    car.vehicle_info()
    print("\n")
