# Warm-up/Review: Answer the following questions the best you can. Treat every
# question separately. If it helps imagine each piece of code is in a different
# file. What will be printed after we run the file?
#
# 1. Write what the following print:
print('1.')
x = 5 + 4
# x is 9
print(x - 4)


# Answer: 5

# 2. What does the following print:
print('\n2.')
x = '5'
# x is '5'
print(x + '0')

# Answer: '50'

# 3. What does the following print:
print('\n3.')
def greet_one():
    print('hello')

x = greet_one() # this is a 'function call'
print("x is {}".format(x))
# Answer: prints 'hello'

# 4. What does the following print:
print('\n4.')
def greet_two():
    return 'hello'

a = greet_two() # this is a 'function call'
# greet_two() -> 'hello'
# a = greet_two()
# a = 'hello'
# What is the value of a here?
print(a)


# Answer:


# 5. What does the following print:
print('\n5.')
def yell(words):
   return words.upper()

loud = yell('hello') # function call -> evaluate the function -> output
# function call: yell('hello'),
# evaluate the function: words.txt = 'hello', 'hello'.upper()
# output: "HELLO"
print(loud)

# Answer:
# Hint: .upper() makes every letter upper case. Ex. "ea".upper() -> "EA"

# 6. What does the following print:
print('\n6.')
def join_swap(w0, w1):
   return w1 + w0

w = join_swap('verse', 're')
# function call: join_swap('verse', 're'),
# evaluate the function: w0 = 'verse', w1 = 're'
# output: w1 + w0 -> 're' + 'verse" -> 'reverse'
print(w)

print(join_swap(w, 'in front of '))
# function call: join_swap(w, 'in front of '),
# evaluate the function: w0 = 'reverse', w1 = 'in front of '
# output: w1 + w0 -> 'in front of' + 'reverse' -> 'in front of reverse'

# Answer:
