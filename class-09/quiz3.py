# Fill out the functions below so that they behave as expected

def example(x):
    """
    >>> example('hello')
    'HELLO'
    """
    print(x.upper())

def one(objects, word):
    """
    >>> fruits = ['oranges', 'apples', 'pineapples']
    >>> one(fruits, 'like')
    I like oranges
    I like apples
    I like pineapples
    """
    # Write your code here
    for next in objects:
        print("I " + word + " " + next)

fruits = ['oranges', 'apples', 'pineapples']
one(fruits, 'like')

def two(prefix, words):
    """
    >>> words = ['start', 'vive', 'ason']
    >>> two('re', words)
    restart
    revive
    reason
    """
    # write your code here
    pass

def sum(nums):
    """ Takes in a list of numbers nums, and returns
    the sum of all numbers.
    >>> sum([1, 2, 3, 4])
    10
    """
    # write your code here
    return
