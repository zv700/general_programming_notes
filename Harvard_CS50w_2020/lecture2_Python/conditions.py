#n = input("Number: ")       

#if n > 0:                   # covers search through positive numbers
#    print("n is positive")
#elif n < 0:                 # covers search through negative numbers, the other half of possible number values
#    print("n is negative")
#else:                       # if n is not positve or negative, it has to be zero 0, the only remaining option
#    print("n is zero")


# Python condition
# stores the input number as variable: n
# Python condition begins with Keyword: if, followed by a boolean expression
# boolean can evaluate to True or False, or some condition that is similar to True or False (like positive or negative) (boolean outcomes can be loosely defined)
# colon: specifies where the beginning of the body of the "if" statement begins, after if *condition* : next line will automatically indent showing it's a python condition (in VSC at least)

# Python REQUIRES indentation to parse specific code, other languages my not require indentation (html does not require indentation)
# indentation shows Python what code is inside the "if" statement (the body of the "if" statement) and what code is outside the "if" statement

# in Python, "else, if" statements are abbrieviated to "elif"
# "elif" and "else, if" are additional "if" statements to check for after the original "if" statement
# the final check in an "if elif else if" chain must be "else"



# DEBUGGING ERROR LOGIC

# python execption = an error that happens because something within our python program did not work correctly
# start from the bottom: "TypeError" = type of error, there's a mismatch of types, Python expected something to be of one type but it ended up being a different type
# "TypeError: '>' not supported between instances of 'str' and 'int' " = greater than symbol > does not work when placed between a string 'str' and an integer 'int', > cannot compare 'str' and 'int'
# > or < only compare integers 'int'
# below "Traceback (most recent call last):" Python gives you the specific line and segment of code where the error occurs
# in line 3: Python thinks "n" within "n > 0:" is a string

# the original input() function doesn't care what you input as an argument, it always gives you a string in return
# input() does not know to give back data in the form of an 'int' integer, it does not know if you typed in a number, letter, etc. by default outputs a string ""
# need to "cast" the output as an 'int' ising int() function  


n = int(input("Number: "))   

if n > 0:                   # covers search through positive numbers
    print("n is positive")
elif n < 0:                 # covers search through negative numbers, the other half of possible number values
    print("n is negative")
else:                       # if n is not positve or negative, it has to be zero 0, the only remaining option
    print("n is zero")