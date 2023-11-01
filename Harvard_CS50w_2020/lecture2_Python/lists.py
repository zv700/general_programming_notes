# order of items/elements matters in a list

# Define a list of names
names = ['Jenny', 'Jamie', 'Jun', 'Jerry']

print(names[1])

names.append('Marge')
names.append('Annie')
# .append adds a value to the end of a list. It's placed following a variable ( variable.append('newValue') )
# .append only takes one argument/input at a time

print(names)

names.sort()
# .sort sorts all of the elements(strings) in a list into alphabetical order

print(names)