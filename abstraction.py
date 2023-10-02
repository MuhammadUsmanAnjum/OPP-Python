# Abstraction is simplifying complex reality by focusing on the essential aspects and ignoring unnecessary details.

# For example, when using a smartphone, you interact with the user interface and functionalities it provides, without needing to understand the intricate technical details of how it works internally. Abstraction allows you to use the smartphone as a tool without needing to know everything about its internal components and processes.


# An abstract class is a class that cannot be instantiated directly and is meant to serve as a blueprint for other classes. It may contain both regular methods with implementations and abstract methods without implementations.

# Abstract methods are declared in the abstract class but lack any concrete code. Abstract methods act as placeholders and must be implemented by concrete (non-abstract) subclasses.

# In Python, the concept of abstract classes and methods is not as rigid as in other languages. We need to use module "abc" for declaring these.



from abc import ABC, abstractmethod

class Shape(ABC):
    # defining an abstract method
    @abstractmethod
    def area(self):
        pass

    # defining a concrete method
    def name(self, name):
      self.name = name
      print(f"The shape is {name}")

# Subclass 'Circle' inherits from 'Shape'
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# Subclass 'Rectangle' inherits from 'Shape'
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Attempting to create an instance of the abstract class 'Shape'
# This will result in a TypeError since abstract classes cannot be instantiated
#shape = Shape()  # Uncommenting this line will raise an error

# Creating instances of concrete subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Using the 'area' method of the subclasses
print("Circle Area:", circle.area())       # Output: Circle Area: 78.53975
print("Rectangle Area:", rectangle.area())  # Output: Rectangle Area: 24
rectangle.name("rectangle")