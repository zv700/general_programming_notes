# two connected files: one file/module that defines a function(functions.py), another file(this one) that calls the function/uses the function defined in the other file
# both methods accomplish same task, method 2 might be useful if you need more than one function from a specific .py file/module

# METHOD 1: import one specific function from another .py file
from functions import square

for i in range(10):
    print(f"The square of {i} is {square(i)}.")

# NameError: name not defined ==> must import function from other file
# from fileName import functionName
############################################################

# METHOD 2: import an all of the code from another .py file/module

import functions

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}.") 

# to use a function from an imported .py file/module, you must specify the imported file name and the function name
# Above: functions.square()
# importedModuleName.functionName()

