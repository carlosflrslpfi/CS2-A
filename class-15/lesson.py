# To read a file we need to open the file
f = open('anniehall', 'r') # return a file object

# The read function reads the entire file
text = f.read()

print("There are {} character in the script".format(len(text)))

words = len(text.split(" "))
print("There are {} words in the script".format(words))

print(f.closed)
f.close() # this ensures that the file is properly closed
print(f.closed)

print("\nUsing with keyword")

# It is good practice to work with files with the 'with' keyword
with open('anniehall', 'r') as f:
    text = f.read()
    print("There are {} character in the script".format(len(text)))
    words = len(text.split(" "))
    print("There are {} words in the script".format(words))
print(f.closed)

# We can also read files line by line
with open('anniehall', 'r') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)


# This is rather inefficient so we can use a loop for it
with open('anniehall', 'r') as f:
    print("All the lines that contain the word funny: ")
    for line in f:
        if 'funny' in line:
            print(line)

