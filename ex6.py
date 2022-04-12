#x = _ creates a variable.
types_of_people = 10
#line 4 creates a variable for a string.
x = f"There are {types_of_people} types of people."
#line 5 and 6 creates new variables
binary = "binary"
do_not = "don't"
#line 9 creates a variable of a string containing the variables created from lines 6 and 7.
y = f"Those who know {binary} and those who {do_not}."

#lines 11 and 12 prints the strings that variables x and y represent.
print(x)
print(y)

#Lines 17 and 18 print a string containing the variables x and y which already contain a string containing variables.
#its a variable inside of a variable inside of a variable *queue x-files music*
print(f"I said: {x}")
print(f"I also said: '{y}'")

#line 21 sets a variable of hilarious to equal False, false has to be capitalized
hilarious = False

#line 24 sets a variable of the joke evaluation, the brackets represent a variable that needs to be added and formatted.
joke_evaluation = "Isn't that joke so funny?! {}"
#.format() formats an already created string.
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
#you can add two variables together to create a long string as seen in line 31.
print(w + e)
