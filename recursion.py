# Recursion is a programming technique where a function calls itself to solve a problem by breaking it into smaller instances of the same problem. It involves two essential components:
# Base Case: The condition that stops the recursion. It provides a straightforward solution for the simplest form of the problem.
# Recursive Case: The function calls itself with modified parameters, approaching the base case step by step.


def factorial(n):
    if n == 0 or n == 1:    # Base case: factorial of 0 is 1
        return 1
    else:             # Recursive case
        return n * factorial(n - 1)

result = factorial(5)  # 5! = 5 * 4 * 3 * 2 * 1
print(result)




def fibonacci(n):   #f(n) = f(n-1) + f(n-2)
  if n==0:
    return 0
  elif n==1 or n==2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(5)


