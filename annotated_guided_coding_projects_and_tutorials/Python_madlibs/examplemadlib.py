# From: https://www.youtube.com/watch?v=8ext9G7xspg&t=100s --> Kylie Ying

# string concatenation = putting strings together, combining words to make strings in a program using plus signs +, can be strings "this is a Python string" or variables whose value you set
# string variables are stored within double quotes ""

########################
##### EXAMPLE TASK #####
# create a string that says "subscribe to ___" --> subscribe to X YouTuber
########################

# youtuber --> is a variable, the variable's value is set to the value of the string ""
# youtuber = "Jenny James"


######## multiple ways to accomplish

# 1
# print("Subscribe to " + youtuber + "!") # string + variable concatenation --> comebine the string: "subscribe to" with the value of the variable: youtuber --> you set the value for youtuber variable, can change depending on user input

# 2
# print("Subscribe to {}!".format(youtuber)) # pulls value of youtuber in .format(youtuber) and places that value within the curly brackets {} inside of the string: "subscribe to {}"

# 3 fstring = formatted string
# print(f"Subscribe to {youtuber}!") # fstring is a string preceded by an f, place curly braces inside of the string where you want a value that can change depending on input value, place the variable that can change within the curly brackets {youtuber}

### Test by running in terminal --> cd to project directory --> run in commandline: python madlibs.py --> no errors = OK!
# python3 command in commandline DOES NOT work in Windows, only works in OSX or Linux because they have Python installed by default --> run just "python" in commmandline on Windows/PC

############################
##### END EXAMPLE TASK #####
############################

#################################################################################################

##############################
##### MADLIBS START HERE #####
##############################


### FIRST print madlib with blanks in a regular string, so the user has context as to where their inputs fit into the madlib
madlib = "The weather is so *adjective* today! Days like this \
make me want to *verb1*! I love to *verb2*, when the weather is *adjective* as well. \
I heard that *famous person's name* also likes to *verb2*."

print(madlib)

### SECOND take user input
adj = input("Adjective: ") # input() function takes user input, "Adjective: " inside of the argument parentheses () prompts user by telling them what to write as an input. User input is stored as variable: adj
verb1 = input("Verb: ") # string text appearing inside of the parameter parentheses () will appear in commandline as placeholder text 
verb2 = input("Verb: ")
famous_person = input("Famous person's name: ")

### THIRD print madlib as an fstring including all of user's inputs
        # use break \ to tell Python the string has gone on to the next line --> still all one string, string continued on next line
madlib = f"The weather is so {adj} today! Days like this \
make me want to {verb1}! I love to {verb2}, when the weather is {adj} as well. \
I heard that {famous_person} also likes to {verb2}."
        # because all of above is one long string over multiple lines, there should be no indentations at the start of each line. In Python, indentations are important for code structure

print(madlib)
