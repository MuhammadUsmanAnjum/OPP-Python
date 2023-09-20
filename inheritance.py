# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows you to create a new class based on an existing class. Inheritance enables code reuse, promotes a hierarchical structure of classes, and allows you to create specialized classes from more general ones.

# Parent Class/ Base Class/ Superclass: the class that you're inheriting from. It defines a set of attributes and methods that can be shared by its subclasses.

# Child Class/ Derived Class/ Subclass: the new class you're creating. It inherits attributes and methods from the base class and can also have its own attributes and metho


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Vehicle Brand is {self.brand} and Model no is {self.model}")

class Car(Vehicle):
    def honk(self):
        print("Honk honk!")

# Creating instances
car = Car("Toyota", "Camry")     

car.info()
car.honk()

#########################################################################################################################

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)        # Call parent class's constructor
        self.radius = radius          # Initialize subclass-specific attribute

    def area(self):                   # Method Overriding
        return 3.14159 * self.radius ** 2

class Square(Shape):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

shapes = [
    Circle("Circle 1", 5),
    Square("Square 1", 4),
    Circle("Circle 2", 7),
    Square("Square 2", 6)
]


for shape in shapes:
    print(f"{shape.name} - Area: {shape.area()} square units")
    
    
    
# Types of Inheritance
# In Python, there are several types of inheritance, each serving different purposes.

# Single Inheritance: A child class inherits from only one parent class. (As shown in the above example.)

# Multiple Inheritance: A child class inherits from more than one parent class.

# Multilevel Inheritance: A child class inherits from a parent class, and another class inherits from this child class.

# Hierarchical Inheritance: Multiple child classes inherit from a single parent class.

# Hybrid Inheritance: Hybrid inheritance is a combination of two or more types of inheritance.


#Single Inheritance
class Vehicle:
    def display(self):
        print("This is a vehicle.")

class Car(Vehicle):
    def display_car(self):
        print("This is a car.")

car = Car()
car.display()
car.display_car()


#Multiple Inheritance
class A:
    def display_A(self):
        print("This is class A.")

class B:
    def display_B(self):
        print("This is class B.")

class C(A, B):
    def display_C(self):
        print("This is class C.")

c = C()
c.display_A()
c.display_B()
c.display_C()



#Multilevel Inheritance
class A:
    def display_A(self):
        print("This is class A.")

class B(A):
    def display_B(self):
        print("This is class B.")

class C(B):
    def display_C(self):
        print("This is class C.")

c = C()
c.display_A()
c.display_B()
c.display_C()



#Heirarchichal Inheritance
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks.")

class Cat(Animal):
    def sound(self):
        print("Cat meows.")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()




#Hybrid Inheritance
class A:
    def display(self):
        print("This is class A.")      # --> Diamond Problem

class B(A):
    def display(self):
        print("This is class B.")

class C(A):
    def display(self):
        print("This is class C.")

class D(C, B):
    def displays(self):
        pass

d = D()
d.display()
d.display()
d.display()
d.displays()



'''write a program that named as Transport whose parameter are name ,
model create a function named as info create another child
class named as Car who derive from Transport has parameter name,
model, speed create a method named as feature then again make a child class
derived from Transport whose properties are name, model and color .
Make another class named as Bus who inherit from Car properties:
name, model, speed size as a parameter. Guess which type of inheritance is this??'''

class Transport:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def info(self):
        print(f"The name of Owner is {self.name} and model is {self.model}")
class Car(Transport):
    def __init__(self,name,model,speed):
        self.speed=speed
        super().__init__(name,model)
    def feature(self):
        print( f" The  {self.model}  has {self.speed}")
class Vehicle(Transport):
    def __init__(self,name,model,color):
        self.color=color
        super().__init__(name,model)
class Bus(Car):
    def __init__(self,name,model,speed,size):
        self.ssize=size
        super().__init__(name,model,speed)

bus =Bus("sara","bmw",20,"small")
car=Car("Ali","Kia",238.9)
bus.info()
car.feature()   


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Vehicle Brand is {self.brand} and Model no is {self.model}")

class Car(Vehicle):
    def honk(self):
        print("Honk honk!")

class Motorcycle(Vehicle):
    def wheelie(self):
        print("Doing a wheelie!")

# Creating instances
car = Car("Toyota", "Camry")
motorcycle = Motorcycle("Honda", "2023")

# Using inherited methods and class-specific methods
car.info()
car.honk()

motorcycle.info()
motorcycle.wheelie()