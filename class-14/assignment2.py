# Answer the following questions in a new python file.
#
# Question 1: Write a function called sum_dictionary_values that
# sums all the values in a dictionary. Assume the values will always be numbers.
# Example:
# >>> stones_songs = {'Start Me Up': 6, 'Wild Horses': 10, 'Angie': 2}
# >>> sum_dictionary_values(stones_songs)
# 18
stones_songs = {'Start Me Up': 6, 'Wild Horses': 10, 'Angie': 2}

def sum_dictionary_values(d):
    s = 0
    for item in d.values():
        s += item
    return s

print(sum_dictionary_values(stones_songs))




# Question 2: Write a function named flatten that takes a list of dictionaries
# and returns a single dictionary. The result should contain all the values from
# the dictionaries in the list in no particular order.
# Example:
# >>> beatles_songs = {'Eleanor Rigby': 3, 'Help': 5, 'Blackbird': 7}
# >>> stones_songs = {'Start Me Up': 6, 'Wild Horses': 10, 'Angie': 2}
# >>> list_of_dictionaries = [beatles_songs, stones_songs]
# >>> flatten(list_of_dictionaries)
# {'Eleanor Rigby': 3, 'Start Me Up': 6, 'Help': 5, 'Blackbird': 7, 'Wild Horses': 10, 'Angie': 2}

def flatten(lst):
    d = {}
    i = 1
    for dictionary in lst:            # outer loop
        print("iteration number {}".format(i))
        print(dictionary)
        i += 1
        for key in dictionary.keys(): # inner loop
            print(key)
            d[key] = dictionary[key]
    return d
# Outer loop:
# 1st iteration: dictionary = beatles_songs
# 2nd iteration: dictionary = stones_songs

beatles_songs = {'Eleanor Rigby': 3, 'Help': 5, 'Blackbird': 7}
stones_songs = {'Start Me Up': 6, 'Wild Horses': 10, 'Angie': 2}
list_of_dictionaries = [beatles_songs, stones_songs]

print(flatten(list_of_dictionaries))

