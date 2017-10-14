# Review

# Booleans
# True, False are Boolean values. They're used by the computer to make decisions.
# Boolean values can be combines with the following operators:

# and - True when both values are True else False
# -> True and True   -> True
# -> True and False  -> False
# -> False and True  -> False
# -> False and False -> False

# or - True when at least one value is True else False
# -> True or True    -> True
# -> True or False   -> True
# -> False or True   -> True
# -> False or False  -> False

# not -> True when False and False when True
# -> not True        -> False
# -> not False       -> True

# Examples:
a = True
b = True
c = (not a) and b  # -> (not True) and True -> False and True -> False
print("c is {}".format(c))

# What's the value of c?

a = False
b = True
c = a or (not b)  # -> False or (not True) -> False or False -> False
print("c is {}".format(c))

# What's the value of c?

# Boolean values are the building blocks of computers. As we all know computers
# use a binary system to carry out operations and represent data. You can
# think of True as 1 and False as 0.


# Control statements
# if <condition>:
#     do something
# else:
#     do something else

# Here <condition> __must__ be a Boolean value i.e. it must evaluate to True/False

# Examples:
a = True
b = False
if a or b:      # a or b, True or False -> True
    print("If!")
else:
    print("Else")

# What's going to be printed?

if not b:      # not b, not False -> True
    print("If!")
else:
    print("Else")

#What's going to be printed?

# Functions -- functions have are routines that can have inputs and outputs.
# We can use functions to process information or trigger a certain routine.

# Examples
def greet(name):
    print("Hello " + name)

# greet("Aaron")
# greet("Amir")
# greet("Lesly")

def add(x, y):
    # Complicated computation
    return x + y

z = add(5, 3)
print(z)

def triple_and(x, y, z):
    return x and y and z  # -> ((x and y) and z)

three_booleans = triple_and(True, False, True)
print(three_booleans)
# Example x = True, y = False, z = True
# ((x and y) and z) -> ((True and False) and True) -> False and True -> False






