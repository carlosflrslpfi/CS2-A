# Question 1: Write a function that takes in a list of names
# and returns a dictionary with each name as a key, and the length
# of the name as the value
def names_to_dict(names):
    """
    names_to_dict(['Jim', 'Jade', 'Maya'])
    {'Jim': 3, 'Jade': 4, 'Maya': 4}
    """
    # Write your code here
    d = {}
    for name in names:
        d[name] = len(name)
    return d
print("Question 1:")
print(names_to_dict(['Jim', 'Jade', 'Maya']))
print()

# Question 2: Write a function that takes in a list of words and a
# dictionary. Replace every occurrence of a key in the list
# with the keys corresponding value, and return the modified list
def replace_words(words, dictionary):
    """
    words = ['hello', 'im', 'very', 'happy']
    d = {'hello': 'hey', 'happy': 'neutral' }
    replace_words(words, d)
    [hey, im, very, neutral]
    """
    new_list = []
    for word in words:
        if word in dictionary:
            new_list.append(dictionary[word])
        else:
            new_list.append(word)
    return new_list
# 1st iteration: word = 'hello', new_list = ['hey']
# 2nd iteration: word = 'im', new_list = ['hey', 'im']
# ...
# end
words = ['hello', 'im', 'very', 'happy']
d = {'hello': 'hey', 'happy': 'neutral' }
print(words)
print(replace_words(words, d))

# Question 3: Write a function that prints a list of words, then using
# the function from Question 2 change a couple words and print the
# newly modified sentence.
# Here are the steps:
# 1. Come up with a sentence and assign it to a variable
# 2. Print the sentence
# 3. Using the your_sentence.split(' ') function turn the item into a list
#       of words.
# 4. Using the list from step 3 and a dictionary, use the function
#       from Question 2 replace some of the words in the sentence
# 5. Using the list returned in step 4 create a sentence using
#       ' '.join(your_list) and print it
# Example output:
# >>> q3()
# 'I like coffee`
# {'I': 'You', 'coffee': 'tea'}
# 'You like tea'
def q3():
    # Write your code here
    s = "hello i like coffee"
    s_list = s.split(" ")
    d = {'coffee': 'juice', 'like': 'dislike'}
    new_list = replace_words(s_list, d)
    print(s)
    print(' '.join(new_list))

q3()

