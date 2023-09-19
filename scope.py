# Scope of a Variable
# Global variable
# Local variable


def fun(y):
  x = 5
  return x+y

fun(2)


# Write a program that inputs a number and give it to a function which then prints its table.
def table(n):
  print(f"Table of {n} from inside the function: ")
  for i in range (1, 11):
    print(f"{n} * {i} = {n}")


num = int(input("Enter a number: "))
table(num)


#Create a function that generates a list of even numbers up to a given limit and returns it.
def even(n):
  a = []
  for i in range(2, n+1, 2):
    a.append(i)
  return a

num = int(input())
even(num)