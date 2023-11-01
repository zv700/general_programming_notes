# "Handle exceptions gracefully."
# program takes a value for x and for y and divides x / y, prints result

import sys      # <== a default Python module

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)


try:                # <== make an attempt to divide/run the program
    result = x / y
except ZeroDivisionError:   # <== contingency plan if this specified situation happens
    print("Error: Cannot divide by 0.") # <== print this error message rather than have the program crash upon error
    sys.exit(1)     # <== exit the program with a status code of: 1, (1 = something went wrong)

print(f"{x} / {y} = {result}")

# if you try to divide by zero you get an exception/program crashes because you can't divide by zero
# ZeroDivisionError = error occurs when you try to divide by zero

# tell program to catch when the user does something wrong and report a nicer looking message instead of a messy Traceback, exception, type of error, etc.
# Exception handler = use "try:" and "except:" conditions to display an error message rather than having the program crash when it runs into an error

# ValueError = error occurs when you input an unacceptable value as an input. 
# Above program only accepts integers int() as inputs. Program will attempt to convert your input (if it's not an integer) into an integer, will fail/crash, and give you a ValueError message

# Use exception handlers if you accept lines of code you are running might run into predictable/anticipatable errors
# If something goes wrong, tell the user what went wrong, rather than just having the entire program crash.
#  
