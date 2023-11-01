# for loop
# this loop is being used to count up starting from zero
for i in [0, 1, 2, 3, 4, 5]:
    print(i)

# Python list that contains six numbers in square brackets
# Python interprets for loop as "go through each element 'in list[]' one at a time in order from left to right. For each element, call that element 'i'. "
# "print the value of 'i' for each iteration of the for loop"

print("space")

# above may be okay for printing/counting up to small numbers, but if counting up to 100 for example, it may be inefficent
# range selects a range of numbers
# below: range(6) will print six numbers starting from zero (does not include the number: 6) (prints 0 through 5 one number at a time)
# below: accomplishes the same thing as the above for loop using a Python list

for j in range(6):
    print(j)

# Python loops can loop through any type of sequence (list, tuple, dictionary, string)

names = ['Jenny', 'Jimmy', 'Jun', 'Jeane']

for name in names:
    print(name)

# above: for loop loops through the list of names, printing the next name with each iteration
# "names" is the variable that the list of names is stored within
# "name" is the variable used to store each individual loop result/each name that is printed with each for loop iteration

color = "turquoise"

for character in color:
    print(character)

# if there's only one item/string stored within a variable, print() will print each individual character/letter

