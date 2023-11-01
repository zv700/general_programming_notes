# decorator = a function that takes a function as an input and returns a modified version of that function as output

# decorators take a function and modifies that function, adds additional behavior to the function, like modifying the value of a number or a string value 
# "functional programming paradigm" = in Python, a function() is a VALUE like any other value, any VALUE in Python can be passed through a function as an input/output
# functionOne(functionTwo())
# functions can not be passed through other functions in other programming languages


####################################################
# DECORATOR
# Create a decorator function that modifies another function by announcing that the function is about to run and that the function has completed running

def announce(f): # <== decorator function: announce() takes function: "f()" as an input and returns a new function as output, decorator function: announce() is taking function: f() and is adding in print statements before and after function: f() runs ==> "wraps up function f() with additional behavior"
    def wrapper(): # function that adds additional behavior to a function known as a "wrapper function"
        print("About to run the function...")
        f() # <== runs function: f()
        print("Done with the function.")
    return wrapper

@announce   # <== @announce adds decorator function: announce() to function: hello() | wraps function: announce() around function: hello() ==> announce(hello())
def hello():
    print("Hello, world!")

hello() # <== runs funciton: hello()


#example use:
# in a web application if you want certain features to run ONLY if a user is logged in ==> write a decorator function that checks if a user is logged in, the apply that decorator to all functions that should only run if logged in
  
