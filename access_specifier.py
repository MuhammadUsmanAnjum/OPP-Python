# Access Specifiers
# In Python, access specifiers are used to control the visibility and accessibility of class attributes and methods.

# Public: By default, all attributes and methods in a class are public, meaning they can be accessed from anywhere.

# Private: Python uses a naming convention to indicate private attributes and methods. Attributes and methods that start with a double underscore (__) are considered private and should not be accessed directly from outside the class.

# Protected: Python uses a single underscore (_) at the beginning of an attribute or method name to suggest that it's intended for internal use within the class and its subclasses.




# class MyClass:
#     def __private_method(self):
#         return "This is a private method"

# obj = MyClass()

# # result = obj.__private_method()
# # print(result)
# obj._MyClass__private_method()



#Protected
# class ProtectedExample:
#     def __init__(self):
#         self._protected_var = "This is a protected variable"

#     def display(self):
#         print(self._protected_var)

# obj = ProtectedExample()
# obj.display()                # Output: This is a protected variable
# print(obj._protected_var)



# class PrivateExample:
#     def __init__(self):
#         self.__private_var = "This is a private variable"

#     def display(self):
#         print(self.__private_var)

# obj = PrivateExample()
# obj.display()  # Output: This is a private variable

# # Access the private variable using name mangling
# print(obj._PrivateExample__private_var)  # Output: This is a private variable






