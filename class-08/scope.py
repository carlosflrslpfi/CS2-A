# Global and local scope
# The place where the binding of a variable is valid.
# Global variable that can be seen and used everywhere in your program
# Local variable that is only seen/used locally.
# Local analogous to within a function.

# we define a global variable x
x = 5

def some_function():
    x = 10 # local variable
    # print('local x is {}'.format(x))
    return x + 5

y = some_function() # Global variable y
# function call: some_function(), no input
# evaluate: x = 10, return x + 5, return 10 + 5
# output: 15
print('global x is {}'.format(x))
# 5, 10, or 15?
print(y)


def other_function():
    a = "hello!"
    print(a)

other_function()
# print(a)

outside_variable = 10

def another_function(x):
    x = x + outside_variable # x = x + outside_variable
    print(x)
    return x + 1

x = 5
print(another_function(x))
# function call: another_function(x), x = 5
# evaluate: x = x + outside_variable, x = 5 + 10 = 15, print(x)
# output: x + 1, 15 + 1, 16

print(x)

def even_yet_another_function(word):
    word = word + ' more letters'
    return word

word = 'hello'
w = even_yet_another_function(word)
# function call: even_yet_another_function(word), word = 'hello'
# evaluate: word = 'hello' + ' more letters' -> word = 'hello more letters'
# return: 'hello more letters'
print(w)
print(word)

# strings are also immutable

# if the data type is an immutable type this works differently.

def make_first_one(lst):
    lst[0] = 1

l = [0, 1]
make_first_one(l)
print(l)

# lists are mutable types
