# Iteration is the repetition of a process.
# For example if I tell you go run around a tree 10 times
# you will be repeating the process of running in a circle for 10 iterations.
laps = 1
while laps < 11:
    print("I'm on lap {}".format(laps))
    laps = laps + 1

# Do not do this
print('\nno loop')
print("I'm on lap 1")
print("I'm on lap 2")
print("I'm on lap 3")
print("I'm on lap 4")
print("I'm on lap 5")
print("I'm on lap 6")
print("I'm on lap 7")
print("I'm on lap 8")
print("I'm on lap 9")
print("I'm on lap 10")

# And the outcome is exactly the same. The only extra thing we
# have to do in the first case is keep track of a single variable

# while loop
# We already looked at this:
# while <condition>:
#     do_stuff()
# if <condition> evaluates to True, do_stuff() repeatedly
# if <condition> evaluates to False, stops the loop
laps = 1
while laps < 11:
    print("I'm on lap {}".format(laps))
    laps += 1
# is laps (1) less than 11? Yes
# is laps (2) less than 11? Yes
# is laps (3) less than 11? Yes
# ...
# is laps (11) less than 11? No, stop the loop.

print("\nfor loop")
# The __for__ loop is very powerful. You can iterate over string, lists, ranges,
# and many more things.
for index in range(1, 11, 2): # range(start, end, step)
    print("I'm on lap {}".format(index))

# For loops can iterate over string
print('\nI am')
s = 'running'
for c in s:
    print(c.upper())

# You can use the for loop to iterate over lists as well.
print()
l = [1, 2, 3, 4, 5]
for num in l:
    print("I'm on lap {}".format((num)))
print("I've still got 5 more laps to go")

# Ranges
print()
print(range(6))
print(list(range(6)))
print()
for i in range(6):
    print("I'm on lap {}".format((i)))
print()
lst = [0, 1, 2, 3, 4, 5]
for i in lst:
    print("I'm on lap {}".format((i)))

# indexing into a string
print()
s = 'running'
for index in range(len(s)):
    print('position: {}, letter: {}'.format(index, s[index]))

# range(len(s)) -> len(s) = 7, range(7)
# index = 0, s[0] -> 'r'
# index = 1, s[1] -> 'u'
# ...
# index = 6, s[6] -> 'g'
