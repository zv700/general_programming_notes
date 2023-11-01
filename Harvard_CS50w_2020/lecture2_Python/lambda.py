# a list (of people) where each element (person) is a dictionary

people = [
    {"name": "Jenny", "house": "Red"},
    {"name": "Javier", "house": "Blue"},
    {"name": "Jieun", "house": "Green"}
]

def f(person):  # <== takes a person (dictionary) as input, function tells .sort() to sort by name alphabetically
    return person["name"] # <== returns that person's name (dictionary's "name" value)


people.sort(key=f) # input: key=f links above function f(person), key= tells .sort() function how to sort, what parameter to use to sort/compare dictionaries

print(people)

# in Python you have the ability to nest data structures within other data structures (example: list inside of list, dictionary inside of list, etc.)
# nesting data structures within others makes it easy to represent data within Python

# type error < not supported between instances of 'dict' and 'dict' ==> people.sort() tries to use < to compare two dictionaries
# Python doesn't know by default how to compare two elements within the list/dictionaries above. .sort() defaulting to comparing numerically 
# each above dictionary has both a "name" and "house" value, so you can tell .sort() to sort by either of those two values
# solve type error by defining a function that tells the .sort() function how to sort, what to compare

print("Above: sorts alphabetically by name. Below: sorts alphabetically by house.")

def f(person):  
    return person["house"] 


people.sort(key=f) # input: key=f links above function f(person), key= tells .sort() function how to sort, what parameter to use to sort/compare dictionaries

print(people)

# Lambda expresson = in Python you can write a short function (def f(person): etc.) as one line of text
# write Lambda expression within the key= argument/input
# below Lambda expression is a condensed version of above

print("Below is sorted with a Lambda expression")

people.sort(key=lambda person: person["name"]) # <== "person:" is the input, person["name"] is the output

print(people)