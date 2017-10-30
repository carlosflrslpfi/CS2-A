
#first question
print("abce" in "abcdefghijklmnopqrstuvwxyz") #returns a Boolean(True or False)


#second question
print("Beast" in "Beast mode activated?") #returns a Boolean(True or False)


#third question
favorite_colors = "blue green red yellow"
favorite_colors.split()
favorite_colors_list = favorite_colors.split() #We need to create a new variable that will store the list we created
print(favorite_colors)
print(favorite_colors_list)


#fourth question
favorite_teams = ["Giants", "Warriors", "Raiders"]
favorite_sports = ["Baseball", "Basketball", "Football"]
favorite_stuff = favorite_teams + favorite_sports #We want to find out what this prints
print(favorite_stuff) #["Giants", "Warriors", "Raiders", "Baseball", "Basketball", "Football"]


#fifth question
pokemon_list = ["Charizard", "Pikachu", "Eevee", "Snorlax", "Magikarp"]
print(pokemon_list[4]) #What index is "Magikarp?
#at 0 == Charizard
#at 1 == Pikachu
#at 2 == Evee
#at 3 == Snorlax
#at 4 == Magikarp


#sixth question
new_pokemon_list = pokemon_list[0:4]
print(new_pokemon_list) # we should expect ["Charizard", "Pikachu", "Eevee", "Snorlax"]



