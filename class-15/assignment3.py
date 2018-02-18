# Q0: go to http://www.simplyscripts.com/a.html and pick a movie you like.
# Create a text file in the same directory as your python file and paste
# the text there. Use this file to complete the following questions:

# Q1: Write a function that counts the number of times the word
# 'universe' is in the script.
def count_universe():
    count = 0
    with open('anniehall', 'r') as f:
        for line in f:
            if 'universe' in line:
                count += 1
    return count
print(count_universe())

# Q2: Write a function that has a words as input and count the number
# of times that word appears in the script.
def count_words(word):
    count = 0
    with open('anniehall', 'r') as f:
        for line in f:
            if word in line:
                count += 1
    return count
print(count_words('funny'))

# Q3: Write a function that creates a dictionary and counts the number
# of times each word in the script is used. Hint: to get a list of
# words from a line use line.strip('\n').split(" ").
def create_counts_dictionary():
    d = {}
    with open('anniehall', 'r') as f:
        for line in f:
            for word in line.strip("\n").split(" "):
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
    return d
print(create_counts_dictionary())

# Q4: Write a function that returns a list of the top n used words.
# Hint 1: to sort a dictionary use:
#   sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
# where 'd' is the dictionary.
# Hint 2: Use the previous function.
def top_n_words(n):
    d = create_counts_dictionary()
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return sorted_d[:n]

print(top_n_words(10)[0])
# evaluate top_n_words(10) -> list[0]
top_n = top_n_words(10)
print(top_n[0])
