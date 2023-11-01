### SAMPLE MADLIB 1: food

madlib = "I'm so hungry. If I could eat anything in the world right now, \
I'd want to eat *noun1*! The taste is so *adjective1*. Some *noun2* would \
be a nice drink to go with my meal. For dessert, *noun3* or maybe *noun4* \
would really hit the spot! I'm absolutely *verb1* thinking about all of the \
food I'm going to eat!"

print(madlib)

# User input:
noun1 = input("Noun 1: ")
adj1 = input("Adjective 1: ")
noun2 = input("Noun 2: ")
noun3 = input("Noun 3: ")
noun4 = input("Noun 4: ")
verb1 = input("Verb 1: ")


madlib = f"I'm so hungry. If I could eat anything in the world right now, \
I'd want to eat {noun1}! The taste is so {adj1}. Some {noun2} would \
be a nice drink to go with my meal. For dessert, {noun3} or maybe {noun4} \
would really hit the spot! I'm absolutely {verb1} thinking about all of the \
food I'm going to eat!"

print(madlib)
print("\n") # prints newline, an empty line after printing last madlib. makes it easier to distinguish between previous and next madlib when next is loaded
