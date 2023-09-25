# Encapsulation
# Encapsulation is the art of enclosing data and its relevant behaviors within a self-contained unit, allowing controlled interaction while hiding internal complexities.

# In simpler words, encapsulation is like placing your data and the actions you can perform on that data inside a protective capsule. This capsule shields the internal complexity and workings of your data, providing a clear and controlled way for other parts of your code to interact with it.

# Properties and Getter/Setter
# Properties and getters/setters are concepts in object-oriented programming that allow you to control how attributes (data) of a class are accessed and modified. They provide a way to encapsulate the interaction with attributes by adding custom logic, validation, and computations. In Python, properties and getters/setters are used to ensure controlled access to attributes, even though Python does not enforce strict access control like some other languages.





class Base:
    def __init__(self, age = 0):
         self.__age = age

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, x):
        self.__age = x

ali = Base()  #instantiation

# setting the age using setter
ali.set_age(21)   #call setter

# retrieving age using getter
print(ali.get_age())

#print(ali.__age)







# Properties:
# Properties provide a way to define special methods for getting, setting, and deleting attributes. They are accessed just like normal attributes, but behind the scenes, the methods you've defined are called. This makes it possible to control attribute access without changing the way you access attributes in your code.

# In Python, properties are created using the property() built-in function or the @property decorator. The property() function takes getter, setter, and deleter methods as arguments, while the decorator allows you to define the getter method directly above the attribute definition.


class person:
    def __init__(self):
        self.__name=''
    def setname(self, name):
        print('setname() called')
        self.__name=name
    def getname(self):
        print('getname() called')
        return self.__name

    def delname(self):
      print("del called")
      del self.__name
    name=property(getname, setname, delname)

p = person()
p.name = "test"
del p.name



# @property Method
class House:

	def __init__(self, price):
		self._price = price

	@property
	def price(self):
		return self._price
	
	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price

		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self._price


house = House(50000.0)
print(house.price)
house.price = 1000.0
print(house.price)
del house.price





