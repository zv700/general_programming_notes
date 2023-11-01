houses = {"Jenny": "Red", "Jimmy": "Blue"}

# when defining a dictionary specify a KEY:VALUE, when defining a dictionary for the first time in a set of code
# "houses" = Dictionary
# "Jenny" = KEY
# "Red" = "Jenny" KEY's corresponding VALUE
# When you look up a KEY, you will recieve the corresponding VALUE

print(houses["Jenny"])

# use square brackets to look up a VALUE associated with a KEY
# dictionaryName["KEY"] = VALUE
# accessing value within a dictionary using square brackets[] is similar to accessing an element within a list also using square brackets[]
# Logic: Take the houses dictionary and look up the value associated with "Jenny"

houses["Johnny"] = "Red"

print(houses)

# Above: add a KEY and VALUE to a dictionary
# Logic: Take the houses dictionary, look up "Johnny", the value for "Johnny" should be "Red"

# Use dictionaries to map one value to another value (example: map a string value to a different string)
