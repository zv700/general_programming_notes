### SAMPLE MADLIB 1: pool

madlib = "There was *noun1* in the pool! The sign clearly says \
not to *verb1* in the pool, but here we are! There were a \
a lot of *noun2*, frantically *verb2* the second they saw *noun1* \
floating up from the middle of the water. The hotel employees kind of \
just stood there *verb3* in confusion the second they saw a stampede of \
poolgoers *verb4* back into the hotel lobby."

print(madlib)

# User inputs: 
noun1 = input("Noun 1: ")
verb1 = input("Verb 1: ")
noun2 = input("Noun 2: ")
verb2 = input("Verb 2: ")
verb3 = input("Verb 3: ")
verb4 = input("Verb 4: ")

madlib = f"There was {noun1} in the pool! The sign clearly says \
not to {verb1} in the pool, but here we are! There were a \
a lot of {noun2}, frantically {verb2} the second they saw {noun1} \
floating up from the middle of the water. The hotel employees kind of \
just stood there {verb3} in confusion the second they saw a stampede of \
poolgoers {verb4} back into the hotel lobby."

print(madlib)
print("\n") # prints newline, an empty line after printing last madlib. makes it easier to distinguish between previous and next madlib when next is loaded
