# define/create a new class in Python
# class = template for a type of object
# below: create a class that represents a Points on a 2d graph that each have an x and y value

class Point():
    def __init__(self, input1, input2):
        self.x = input1 # the "x" value or input1 is stored in property: x, the "y" value or input1 is stored in property: y
        self.y = input2 # names for input1 and input2 can be anything (example: x and y, a and b ), the names of the properties they are stored in are contextually important because Points() on a 2d graph have an "x" and a "y" coordinate

p = Point(2, 8) # created a new point called: "p", p's class is Point()
#print(p.x) # print"access point: p's x value and print it"
#print(p.y) # print"access point: p's y value and print it"
print(f"The point's x value is {p.x}.") 
print(f"The point's y value is {p.y}.")

# new defined class is called Point, can create new objects that are also Points later
# "When I create a new Point()/class object, what should happen?"
# __init__ = "magic method" ==> a function/method that will be called every time I try to make a new Point()/class object of the same label
# all functions that operate on objects themselves (= methods) take the first argument "self" ==> __init__(self, )
        # argument: "self" represents the object itself, provides flexibility (example: two different points on a graph might each have its own x value that is different than other points, if you had the argument "x" instead of "self", you'd have to rewrite x values every time you made a new Point())
        # LINE 13 cont.: value of "self" argument will change automatically depending on the object/Point() you are currently handling, where as "x" would be one static value
        # we are storing "x" values for each point in the objects themselves
# each data Point() stores its own x and y values within itself, "self" argument tells this to Python

# any new class objects of the same name(in this case Point) will automatically recieve all parameters within the class definition
# in context: any new Point() object will have __init__, self.x, self.y without having to write them in. YOU MUST include the defined input values, EXCEPT for "self" argument.
# above: in p = Point(2, 8), 2 = input1 and 8 = input2


################################################
# EXAMPLE usage scenario, OBJECT ORIENTED PROGRAMMING:

# TASK:
# Create a class useful for an airliner/flight scheduling 
# the airline needs to keep track of passengers booking flights
# make sure no flight is overbooked
# (i.e. make sure flights are only booked to capacity, passengers cannot book the flight if it is full)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity # storing the value of "capacity" parameter within the Flight() itself
        self.passengers = [] # creates an empty list of passengers, will become populated as passengers book the flight

    def add_passenger(self, name):
        if not self.open_seats(): # <== same as saying "if self.open_seats() == 0" ==> if there are not any open seats
            return False # if there are no open seats, returns False (an error)
        self.passengers.append(name) # self.passengers = an attribute of object Flight() | .append adds each passenger's name to the above list: self.passengers = []
        return True # returns true if you were able to successfully add a new passenger/a passenger was able to book the flight because there were open seats available


    def open_seats(self):   # need function/method open_seats() because otherwise, you would be able to keep adding new passengers beyond the maximum capacity
        return self.capacity - len(self.passengers) # function open_seats() tells you the capacity(total seats) - the length of self.passengers(how many people booked the flight) = number of open seats

flight1 = Flight(3) # <== capacity = 3, 3 people can book the flight

# takes argument "capacity", every flight needs to know the maximum number of people that can fit on a plane

people = ["Josephina", "Jeremy", "Jieun", "Javier", "Jordan", "Jenny"]
for person in people: # <== line defines each item within list: people, as a value called: person
    
    #METHOD 1
    #success = flight1.add_passenger(person) # <== line attempts to call the function: flight1.add_passenger() to add each person in the list as a passenger on flight1 and then saves the result (True or False) in variable: success
    #if success: # <== if variable success evaluates to True
    #    print(f"{person} was added to the flight successfully.") 
    #else:   # <== otherwise, if variable success evaluates to False
    #    print(f"No seats are currently available. {person} was not added to the flight.")
     # <== line attempts to call the function: flight1.add_passenger() to add each person in the list as a passenger on flight1 and then saves the result (True or False) in variable: success
    
    #METHOD 2 <== one less line of code because it skips unnecessary step of defining variable: success, accomplishes same task as METHOD 1
    if flight1.add_passenger(person): # <== if flight1.add_passenger() evaluates to True
        print(f"{person} was added to the flight successfully.") 
    else:   
        print(f"No seats are currently available. {person} was not added to the flight.")
