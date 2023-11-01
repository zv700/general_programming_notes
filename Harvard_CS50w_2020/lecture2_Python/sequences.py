name = "Harry"

print(name[2 * 2])


# many types of sequences with similar properties
# a string is a type of sequence
# can access elements within a sequence (like an array within JavaScript)
# square bracket indexing notation allows access to one specified element within an ordered sequence
# print(name[0]) will print the first character/letter in the string "Harry" which is "H"
# since there is only one string within variable: name, print(name[]) will grab characters/letters in the numbered position you specify

# if you do math within print(name[]) it will print the character in the position of the answer
# example: print(name[2*2]) will print the character/letter that is the 4th in the sequence: "y"

morenames = ['Jimmy', 'Jamie', 'John']

print(morenames)
print(morenames[0])

# can store multiple values in a sequence within a variable using a list
# because variable: morenames contains multiple strings within an array, print(morenames[]) will grab the string in the specified numbered position
# each string in an list/array must be contained within its own set of single' ' or double " " quotation marks and seperated by a comma
# in lists you use square brackets [] with commas between each value 


coordinateX = 10.0 # <== instead of defining two different variables, make a tuple
coordinateY = 20.0

coordinate = (10.0, 20.0) # <== a tuple that accomplishes the same thing as above two variables in one

# tuple is used when you have a couple values that aren't going to change, but you need to store a pair of values (like when graphing in two dimensions needing an x and y value for one unit)
# in tuples you use parentheses () with commas between each value 