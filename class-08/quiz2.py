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

# x = 'aa2', x[0] -> 'a', x[1] -> 'a', x[2] -> '2'
def example():
    """ example() returns 7 """
    return mystery('aa')
    # return mystery1("aa2", 10) # -> 2 + (10 / 2) -> 2 + 5 -> 7

def a():
    """ a() returns 10 """
    # write your code here
    return mystery('aeril')

def b():
    """ b() returns 17 """
    # write your code here
    return a() + mystery1('ae4', 6)
# a() -> 10
# mystery1('ae4', 6) -> word = 'ae4', num = 6
# int(word[2]) -> 4, num / 2 -> 3
# 4 + 3 = 7

def c():
    """ c() returns 100 """
    # write your code here
    return


if __name__ == "__main__":
    print("example() -> {}".format(example()))
    print("a() -> {}".format(a()))
    print("b() -> {}".format(b()))
    print("c() -> {}".format(c()))
