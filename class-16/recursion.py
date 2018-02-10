# Recursion is a method of solving a problem, where the solution
# to the problem depends on solving smaller instance of the problem.

# Example: factorial:
# Factorial in mathematics is a positive integer n, denoted n! which
# is the product of all positive integers less than or equal to n.
# For example: 5! = 1 x 2 x 3 x 4 x 5

# Let's first write a function that calculates factorial
def factorial1(n):
    """ Calculates n! """
    return

# Let's write out the first couple factorial numbers
# n = 1, 1! = 1
# n = 2, 2! = 1 x 2
# n = 3, 3! = 1 x 2 x 3
# n = 4, 4! = 1 x 2 x 3 x 4
# n = 5, 5! = 1 x 2 x 3 x 4 x 5
# n = 6, 6! = 5! x 6 --> Using recursive relation
# n = 7, 7! = 6! x 7 --> Using recursive relation

def factorial2(n):
    """ Recursively calculates n! """
    return

# Base case: is the simplest form of our problem, when you can solve it in
# one step. It is also what stops the recursion from running infinitely
# Recursive case: is where we invoke the same function we're defining
# to attempt to solve our problem. Here we also use the current values
# to build a solution for the problem. For mathematical function we usually
# look at the recursive relation of the problem to solve it.


# Fibonacci sequence is an integer sequence where every number after the
# first two is the sum of the two preceding numbers.
# Fibonacci sequence:
#   1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# What are the base cases?
# n = 0, fibonacci(1) = 1
# n = 1, fibonacci(2) = 1
# The recursive relation looks something like this:
#   fibonacci(n) = fibonacci(n-2) + fibonacci(n-1)

# Write a recursive function that calculates the nth fibonacci number.
def fibonacci(n):
    """ Calculates the nth fibonacci number. """
    return
