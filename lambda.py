# In Python, a lambda function is a small, anonymous function that can have any number of arguments but can only have one expression.


# #Normal Function
# def product(x):
#     return x * 2
# print(product(4))

# #Using Lambda Function
# product = lambda x: x * 2
# print(product(4))


# #Sum function using Lambda

# add = lambda x, y: x + y
# print(add(3, 9))



# # Lmabda function with higher order functions
# def new_func(x):
#   return lambda y,z : y*z*x

# var = new_func(2)
# output = var(3,4)
# print(output)



add = lambda x, y: x+y
subtract = lambda x, y : x-y
def apply_operation():
  return lambda op, value1, value2: op(value1, value2)

sum_result = apply_operation()
print(sum_result(add, 5, 3))