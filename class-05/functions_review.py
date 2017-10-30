# Using a combination of __only__ the functions defined and math __operations__ fill out
# the functions below so that the code produces the correct output.

# Copy and paste the everything on this note into a new python file if you want to run
# it on PyCharm. I suggest trying to answer the questions by reading and understanding the code
# rather than running it.

def mystery(word):
    """ Takes in a word and returns the number of letters in it plus 5. """
    return len(word) + 5

def mystery1(word, num):
    return int(word[2]) + num / 2

def example():
    """ example() returns 7 """
    return mystery("aa")

def a():
    """ a() returns 10 """
    # write your code here
    return mystery("abcde")

def b():
    """ b() returns 17 """
    # write your code here
    return mystery1("ac5", 10) + mystery("aa")

def c():
    """ c() returns 100 """
    # write your code here
    return mystery1("aa5", 190)


if __name__ == "__main__":
    print("example() -> {}".format(example()))
    print("a() -> {}".format(a()))
    print("b() -> {}".format(b()))
    print("c() -> {}".format(c()))
