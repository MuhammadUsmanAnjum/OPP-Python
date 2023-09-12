# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.


def my_func(): 
  print("Hello World from inside of a function.")

my_func()



# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

def my_func(a):   # a is "Parameter"
  print("Hello", a)

my_func("Pakistan")
my_func("India")
my_func("America")



# Parameters vs Arguments
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

def name(first, last):
  print("I'm", first, last, ".")

name("Hijab", "Naqvi")



# Arbitrary Arguments (*args)
# If number of arguments isn't known before, a * can be used before parameter in function definition. In this way, the function will accept a tuple of arguments.

def my_name(*name):
  print("My name is",name[2] )

my_name("Hijab", "Amna", "Ali")



# Keyword Arguments (kwargs)
# To avoid order of arguments, use key=value syntax to send arguments.

def my_name(name1, name2, name3):
  print("I'm", name1)
my_name(name3 = "Hijab", name1 = "Amna", name2 = "Ali")


def my_name(**name):
  print("I'm", name['name1'])

my_name(name1 = "Hijab", name2 = "Amna", name3 = "Ali")



# return values
# Use print when you want to show a value to a human. return is a keyword. When a return statement is reached, Python will stop the execution of the current function, sending a value out to where the function was called. Use return when you want to send a value from one point in your code to another.

def my_function(x):
  return 5 * x



# Higer Order function
# A higher-order function is a function that takes one or more functions as arguments or returns a function as a result. In simpler terms, a higher-order function either accepts functions as inputs or produces functions as outputs.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def apply_operation(operation, value1, value2):
    result = operation(value1, value2) #add(5,3)
    return result

Sum_result = apply_operation(subtract, 5, 3)
print(Sum_result)









