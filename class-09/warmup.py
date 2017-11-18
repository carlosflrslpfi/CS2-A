
# 1. Write what the following print:
print("Q1:")
# x = 10
# while True:
#     print(x)
# Answer: prints 10 forever

# 2. What does the following print:
print("\nQ2:")
c = ""
for i in range(5):
    c = c + str(i)   # c = c + str(i)
    print("i: {}, c: {}".format(i, c))
print(c)
# Answer:
# Hint: range(x) returns the sequence 0, 1, 2, ..., x-1
# range(5) -> 0, 1, 2, 3, 4
# iterations, value of c
# i = 0: c = "", c = "0"
# i = 1: c = "0" + "1" = "01"
# i = 2: c = "01" + "2" = "012"
# i = 3: c = "012" + "3" = "0123"
# i = 4: c = "0123" + "4" = "01234"

print("\nQ3:")
# 3. What does the following print:
def do_something(word):
    for l in word:
        print(l)

do_something('tea')
# Answer:
# word = 'tea'
# iteration 0: l = 't'
# iteration 1: l = 'e'
# iteration 2: l = 'a'



# 4. What does the following print:
print("\nQ4:")
def w(x):
    for i in range(x): # 0, 1, 2, ..., x-1
        if i % 2 == 0: # is i an even number?
            print(i)

x = 6
w(x)
# What should the value of x be for the code to prints:
# 0
# 2
# 4
# Answer:
# Hint: % is the modulo operator, Example: x % y returns the remainder of diving the x by y in the example above it is asking "is this an even number?"
# i = 0, is 0 % 2 == 0? prints 0
# i = 1, is 1 % 2 == 0?
# i = 2, is 2 % 2 == 0? prints 2
# i = 3, is 3 % 2 == 0?
# i = 4, is 4 % 2 == 0? prints 4
# i = 5, is 5 even?

# range(5) -> 0, 1, 2, 3, 4
# i = 0
# i = 1
# i = 2
# i = 3
# i = 4

# 5. What does the following print:
print("\nQ5:")
letters = ['A', 'w', 'w']
def blop():
    s = ""
    for c in letters:
        s += c # s = s + c
    return s + 'ducational'

word = blop()
print('www.reddit.com/r/' + word)
# Answer:
# iter 0: c = 'A', s = '' + 'A' = 'A'
# iter 1: c = 'w', s = 'A' + 'w' = 'Aw'
# iter 2: c = 'w', s = 'Aw' + 'w' = 'Aww'
# s = 'Aww' returning -> s + 'ducational' = 'Awwducational'
# 'www.reddit.com/r/Awwducational'
