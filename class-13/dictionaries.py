# Dictionaries are a data structure. Similar to lists
# dictionaries hold values for us. A dictionary items are
# a collection of key, value pairs.
d = {} # or d = dict()
d['key1'] = 'value1'
d['key2'] = 'value2'
print()

# To retireve the __values__ in a dictionary you have to
# use the bracket notation with the __key__ as input
print(d['key1']) # prints 'value1'
print(d['key2']) # prints 'value2'
# using d.get(key) also works
print(d.get('key1'))
print(d.get('key2'))
print()

# Dictionaries can also be initialized with values
d = {'key1': 'value1', 'key2': 'value2'}
print(d['key1'])
print(d['key2'])
print()

print(d.keys()) # Iterable of keys (think of it as a list)
print(d.values()) # Iterable of values
print(d.items()) # Iterable of key,value pairs
print()

print("Keys:")
for key in d.keys():
    print(key)
print()

print("Values:")
for val in d.values():
    print(val)
print()

print("Key, Value pairs")
for key, val in d.items():
    print("Key: {}, Value: {}".format(key, val))
print()

# Example of building a dictionary
scores = {}
num = 60
for assignment in ['hw', 'quiz', 'test']:
    scores[assignment] = num
    num += 20
print(scores)
print()

# You can also change items in a dictionary just like a list
d = {2: '', 4: '', 5: ''}
for k in d.keys():
    if k % 2 == 0:
        d[k] = 'even'
    else:
        d[k] = 'odd'
print(d)

# you can check if a key is in a dicitonary
print(2 in d)
print(10 in d)
