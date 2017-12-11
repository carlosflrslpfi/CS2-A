def a(l):
    new_l = []
    for letter in l:
        new_l = [letter] + new_l
    return new_l

print("Q1:")
# Should print ['3', '2', '1']
print(a(['1', '2', '3']) )


def my_sum(nums):
    """ Sums all the numbers in a list """
    # YOUR CODE HERE
    n = 0 # this will hold the total sum
    for num in nums:
        n += num
    return n

print("\nQ2:")
print(my_sum([2, 4, 6]))

def reverse(s):
    """ Reverses a string """
    # YOUR CODE HERE
    reversed_s = "" # this will hold the revese string
    for letter in s:
        reversed_s = letter + reversed_s
    return reversed_s
# Note how the reverse function is very similar to the first question.

print("\nQ3:")
print(reverse("code"))
