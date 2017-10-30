#Introduction to Lists

#Lists can be composed of integers, floats, strings, more lists, and more things.

list_name = ["cooking", "washing", "chores"] #Each item is separated with a comma ","
print(list_name)

#Examples of a list

odd_numbers = [1,3,5,7] #list of integers
favorite_colors = ["blue", "red", "orange", "brown"] #list of strings
money_spent = [12.00, 6.00, 5.00, 2.00] #list of floats

#Using the in operator
if("games" in "you got games?"): #checking if "games" is in "you got games?"
    print("True")
else:
    print("False")
# string in string return True or False
#print(string in another_string"")

if("games" in "you got games?"): #checking if "games" is in "you got games?"
    print("True")
else:
    print("False")


print("games" in "you got games?")

print("blue" in favorite_colors)
print("black" in favorite_colors) #Is black in our favorite colors list?

#.split()
#We use the .split() to turn a string into a list of strings
games_string = "You got games?"
games_list = games_string.split()
print(games_string) #prints "You got games?"
print(games_list)   #print ["You", "got', 'games?']

#Concatenation
red_color = "Red"
blue_color = "Blue"
all_colors = red_color + blue_color
diff_color = blue_color + red_color
print(all_colors)
print(diff_color)

cities = ["Berkeley", "San Francisco", "Los Angeles"]
states = ["California", "Florida", "Texas"]
cities_states = cities + states #this concatenating two lists that are composed of strings
print(cities_states)

odd_numbers = [1,3,5,7]
even_numbers = [2,4,6,8]
numbers = odd_numbers + even_numbers
print(numbers)

#Indexing
my_age = [0,1,2,3,4,5,6,7,8,9,10]
print(my_age[0])
cities = ["Berkeley", "San Francisco", "Los Angeles"]
print(cities[1]) #prints "San Fancisco"
#name_of_list[INDEX]
favorite_colors = ["blue", "red", "orange", "brown"] #index of blue is 0, index of red is 1, index of orange 2, index of brown 3
print(favorite_colors[3])

#Delimeters  putting ":" into the [], so that would look like [:]
#name_of_list[a:b] a and b could be any number. a<="stuff that is in the middle"<b
favorite_colors = ["blue", "red", "orange", "brown"]
print(favorite_colors[0:1]) # prints ['blue']
print(favorite_colors[2:3]) #prints ['orange']
print(favorite_colors[1:3]) #prints ['red', 'orange']

my_age = [0,1,2,3,4,5,6,7,8,9,10]
print(my_age[0:7])
print(my_age[:7]) #we are leaving a blank
print(my_age[6:]) #we are leaving b blank, Starts from 6 and goes until the ends of the list
#when we leave both sides blank
print(my_age[:])
animal = ['cat', 'dog', 'monkey', 'dragons']
print(animal[0:2]) #['cat', 'dog']
print(animal[:2])
print(animal[1:3]) #['dog', 'monkey']




