### SAMPLE MADLIB 1: xmas

madlib = "The weather outside is *adjective1*, but the fire is so *adjective2*. \
If we've no place to *verb1*; let it *verb2*, let it *verb3*, let it *verb4*!"

print(madlib)

# User inputs: 
adj1 = input("Adjective 1: ")
adj2 = input("Adjective 2: ")
verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
verb3 = input("Verb 3: ")
verb4 = input("Verb 4: ")

madlib = f"The weather outside is {adj1}, but the fire is so {adj2}. \
If we've no place to {verb1}; let it {verb2}, let it {verb3}, let it {verb4}!"

print(madlib)
print("\n") # prints newline, an empty line after printing last madlib. makes it easier to distinguish between previous and next madlib when next is loaded 

