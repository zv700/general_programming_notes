# order of elements/items does not matter within a set
# all values within a set must be unique

# Create an empty set, a set can exist without containing any values
s = set()  # "s" is the variable where the empty set is stored within 

# Add elements to the set
s.add(1)  
s.add(2)  # use .add command to add values to a set
s.add(3)
s.add(4)
s.add(3)  # <== adding "3" to the set a second time will not make "3" show up more than once when the program is run
print(s)  # no element ever appears more than once in a set, similar to math definition of a set

s.remove(2) # use .remove to remove values from a set
print(s)

#"len" command will give you the length of an item, (number of items within a list, number of characters making up a string, number of elements inside of a set)

print(f"The second set has {len(s)} elements.") # formatted string/fstring: within curly braces you can include any expression usable within Python that you'd like to substiute into the middle of a string.
# len(s) is used to find how many elements are within set: s
# when placed in curly braces of formatted string, the completed calculation will replace the curly braces when program is run/printed
