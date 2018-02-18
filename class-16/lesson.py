# Recursion is a method of solving problems, where the solution
# to the problem depends on solving smaller instances of the problem.

# Example: Factorial.
# Factorial in mathematics is a positive integer n, denoted by n! which
# is the product of all positive integers less than or equal to n.
# For example: 5! = 5 x 4 x 3 x 2 x 1 ...

# Let's first write a function that calculates this
def factorial1(n):
    """ Calculates n! """
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
    return prod

print(factorial1(3))
print(factorial1(5))
print(factorial1(7))
# factorial1(3) ->
# range = [1, 2, 3]
# 1st iteration, prod = 1, i = 1, prod = 1
# 2nd iteration, prod = 1, i = 2, prod = 2
# 3rd iteration, prod = 2, i = 3, prod = 6
# 3! = 3 x 2 x 1 = 6

# range(k, n) -> [k, ..., n-1]
# n = 3
# range(1, 4) -> [1, 2, 3]

# n = 2 -> [1, 2]
# n = 5 -> [1, 2, 3, 4, 5]
# first iteration, i = 1
# second iteration, i = 2

# Let's write out the first couple factorial numbers
# n = 1, 1! = 1
# n = 2, 2! = 1 x 2
# n = 3, 3! = 1 x 2 x 3
# n = 4, 4! = 1 x 2 x 3 x 4
# n = 5, 5! = 1 x 2 x 3 x 4 x 5
# n = 6, 6! = 5! x 6 -> using recursive relation
# n = 7, 7! = 6! x 7 -> using recursive relation

# n, n! = (n-1)! x n

def factorial(n):
    """ Recursively calculates n! """
    if (n == 1): # base case
        return 1
    else:
        return factorial(n-1) * n # recursive case

print(factorial(3))

# n = 3,
# factorial(3) -> factorial(3) * 3
# factorial(3) -> factorial(3) * 3
# ... forever
# factorial(3) -> factorial(3) * 3
# infinite recursion

# n = 3,
# factorial(3) -> factorial(2) * 3 -> 6
# factorial(2) -> factorial(1) * 2 -> 2
# factorial(1) -> 1                -> 1

# Base case: is the simplest form of our problem, when you can solve it
# in one step.
# Recursive case: is where we invoke (or call) the same function we're
# defining to attempt to solve our problem. Here we also user the current
# values to build a solution for the problem.
# We usually want the inputs to the the recursive call to get
# closer to the base case, to stop the recursion.


# Fibonacci sequence is an integer sequence where every number after the
# first two is the sum of the two preceding numbers.
# Fibonacci sequence:
#            n =  0, 1, 2, 3, 4, 5, 6,  7,  8,  9,  10, 11
# fibonacci(n) =  1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...

# n = 3, fibonacci(n) = 3
# n = 8, fibonacci(n) = 34

# What are the base case(s):
# n = 0, fibonacci(0) = 1
# n = 1, fibonacci(1) = 1
# n = 2, fibonacci(2) = 1 + 1 = 2
# n = 3, fibonacci(3) = 1 + 2 = 3
# n = 4, fibonacci(4) = 2 + 3 = 5
# ...
# The recursive relation looks like this:
#   fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)














