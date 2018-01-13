# Dictionaries are a data structure. Similar to lists, they hold
# values for us.
l = [1, 2, 3, 4, 5]
# A dictionary holds items in a key, value pair.
d = {} # or d = dict()
d['key1'] = 'value1'
d['key2'] = 'value2'
print(d) # {'key1': 'value1', 'key2': 'value2'}
print(d) # {'key2': 'value2', 'key1': 'value1'}
print()

# To retrieve the __values__ in a dictionary you have to use
# the bracket notation with __key__ as input
print(d['key1'])
print(d['key2'])
# using d.get(key) also works
print(d.get('key1'))
print(d.get('key2'))
print()

# dictionaries can also be initialized with values
d = {'key1': 'value1', 'key2': 'value2'}
print(d['key1'])
print(d['key2'])
print()

print(d.keys()) # Iterable of keys (think of this as a list)
print(d.values()) # Iterable of values
print(d.items()) # Iterable of key, value pairs
print()

print("Keys:")
for key in d.keys():
    print(key)
print()

print("Values:")
for val in d.values():
    print(val)
print()

print("Key, value pairs:")
for key, val in d.items():
    print("Key: {}, Value: {}".format(key, val))
print()

# Example of building a dictionary
scores = {}
num = 60
assignments = ['hw', 'quiz', 'test']

for task in assignments:
    print(task)
# 1st iteration: assignment = 'hw'
# 2nd iteration: assignment = 'quiz'
# 3rd iteration: assignment = 'test'

for task in assignments:
    scores[task] = num
    num += 20 # num = num + 20
print(scores)
print()
# 1st iteration: {'hw': 60}
# 2nd iteration: {'hw': 60, 'quiz': 80}
# 3rd iteration: {'hw': 60, 'quiz': 80, 'test': 100}

# You can also change items in a dictionary just like a list
d = {2: '', 4: '', 5: ''}
# We want the values to be either odd or even, depending on the key
# if the key is an even number, the value should be 'even'
# if the key is an odd number, the value should be 'odd'
for k in d.keys():
    if k % 2 == 0: # basically saying is this even?
        d[k] = 'even'
    else:
        d[k] = 'odd'
print(d)
print()
# Before the loop: {2: '', 4: '', 5: ''}
# 1st iteration: {2: 'even', 4: '', 5: ''}
# 2nd iteration: {2: 'even', 4: 'even', 5: ''}
# 3rd iteration: {2: 'even', 4: 'even', 5: 'odd'}

# you can also check if a __key__ is in a dictionary
print(2 in d)
print(10 in d)

# I want to know if the word 'even' is in dictionary d as a __value__
print('even' in d) # false because 'in' only looks at keys
print('even' in d.values())

# mod operation, modular arithmetic
# k % 2, divide k by 2, and return the remainder.
# if there's no remainder that means that k is divisible by 2



