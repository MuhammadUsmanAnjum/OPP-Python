# Object Oriented Programming
# Why OOP is used in programming languages?

# Python is an objected oriented language. What does it mean?


# Classes/ Objects
# Python is an object oriented programming language which means that everything in it is an object with its properties and methods.

# In Python, each data type is an object that has been instantiated earlier by some class.

# If we want to create a data type of our own, we'll make a class for it, and will define its attribut


# Instance = Object
# Attribute = Properties
# Methods = Functions in class


class Person:    # a class named 'Person' is created.
  name = "Ali"    # class 'Person' has a property 'name'.

p1 = Person()   	# an object 'p1' of class is created.
print(p1.name)


# Object Methods
# A function inside a class that is related to an object is called Method.

# Important: Self is the mandatory first parameter of a method which can also be named anything (but using 'self' is a convention).

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.


class Sum:

  def add(self, num1, num2):
    result = num1+num2
    print("The sum is:", result)
  def sub(self, num1, num2):
    result = num1-num2
    print("The sum is:", result)


obj1 = Sum()
obj1.sub(9,5)


class Area:
  def calc_area(self, x, y):
    print("The area of this rectangle is:", x*y)

rectangle1 = Area()
rectangle1.width = 5
rectangle1.length = 8

rectangle2 = Area()
rectangle2.width = 6
rectangle2.length = 7


rectangle1.calc_area(rectangle1.width, rectangle1.length)
rectangle2.calc_area(rectangle2.width, rectangle2.length)
         
         
# Constructor
# __init__ method is used as a constructor in Python. It is always executed when the class is being initiated.

# Use the init() function to assign values to object properties, or other operations that are necessary to do when the object is being created.    


class Sum:
  def __init__(self):
    print("I'm executed!")

obj1 = Sum()


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)



# Destructor
# In Python, a destructor is a special method that is called when an object is destroyed.

# Destructors are typically used to perform clean-up tasks, such as releasing resources that were allocated by the object.

# The self parameter in the destructor refers to the object that is being destroyed.


class MyClass:
    def __init__(self):
        print("Hello")

    def __del__(self):
        print("MyClass.__del__()")


obj = MyClass()
print("obj:", obj)
del obj
print("obj:", obj)


