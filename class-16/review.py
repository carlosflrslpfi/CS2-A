# A function is a procedure/process that takes 0 or more inputs and
# produces an output.
# A pure function: always returns the same output for the same inputs

def two():
    return 2

y = two # refers to the function or procedure

print(y)

y = two() # parenthesis __evaluates__ the function or procedure
          # A function call!
          # Not just refer to the procedure but run the procedure
print(y)

d = {}

print(d)
print(type(d))

# d() a dictionary is NOT a procedure so it cannot be evaluated

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(l[:10]) # list slicing l[n:k] includes n through k-1.

