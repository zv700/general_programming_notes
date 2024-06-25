import random
import time

# tutorial source: https://www.youtube.com/watch?v=8ext9G7xspg&t=100s
# timestamp: 1:15:53
# Binary Search "12 Beginner Python Projects - Coding Course" by Kylie Ying, FreeCodeCamp

##########################
##### CONCEPT NOTES ######
##########################

# What is binary search?
    # "Divide and conquer" method of searching through lists
    # looking through a sorted list [least to greatest values] for a specific number[target number]
    # binary search searches the list beginning from the MIDDLE number[midpoint] 
    # if the number is equal to, the search ends, you found the answer
    # if the number does not fit the criteria, you cut the list in two half and only search through the half where the target could be in
        # half that is chosen depends on if the target number is GREATER THAN or LESS THAN the midpoint

#######################################
##### EXAMPLE binary search logic #####
#######################################

    # ex. binary search for number: target = 3
    # RECURSION: after calling binary_search() function, binary_search() will CALL ITSELF automatically until: (1. the target is found) OR (2. it is decided that the target is not in the list)

# FIRST binary_search() function call
    # List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] has a total of 11 elements/numbers -> midpoint = (low(1) + high(11))/2 = 12/2 = 6
    # corresponding indices: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # midpoint, center number of list = 6 [index: 5]
        # does 6 = 3 ? -> no
        # is target < midpoint? = is 3 < 6? yes
            # cut list into two sections: 1. less than midpoint and 2. greater than midpoint
            # because 3(target) < 6(midpoint), only check section 1. less than midpoint
                # new low and high indicies: low = low, high = midpoint[index: 5] + 1 = INDEX: 6 

# SECOND binary_search() function call    
    # New list of values to check: [1, 2, 3, 4, 5, 6, 7]
    # New list's corresponding indicies: [0, 1, 2, 3, 4, 5, 6] -
        # midpoint = 4[index: 3]
            # is 4 = 3 ? -> no
            # is target < midpoint? = is 3 < 4? yes
                # cut list into two sections
                # because 3(target) < 4(midpoint), only check section that is less than midpoint
                    # new low and high indicies: low = low, high = midpoint[index: 4] + 1 = INDEX: 5

# THIRD binary_search() function call
    # etc.


# "naive search" = searching by iterating through a list and checking each individual number one by one

#-------------------------------------------------------------
######################################
##### Beginning of tutorial code #####
######################################
#-------------------------------------------------------------

# Implementation of binary search algorithm

# We will prove that binary search is faster than naive search

# naive search: scan entire list and ask if its equal to the target, [one list item at a time from beginning to end until the target is found]
# if yes, return the index
# if no, then return -1
def naive_search(l, target): # first input is a list named: l [L lowercase], second input is a variable: target
    # example l = [1, 3, 10, 12] -> 10 is target
        # iterating through list: when [i] = 0, [1] is being checked. when [i] = 1, [3] is being checked
        # target found: [i] = 2, 10 is checked. 10 is the target, so the index [i] will be returned, the function will return: 2
    for i in range(len(l)): # for every single index
        if l[i] == target:  # if l at that index[i] is the target, then return that index number
            return i
    return -1 # otherwise we've gone through the entire list without finding the target

# binary search uses "divide and conquer" 
# we will leverage the fact that our list is SORTED to make the search faster
def binary_search(l, target, low=None, high=None): # (low and high are indices [index plural = indicies]) if low and high input criteria are specified, they can be added in later with subsequent binary_search() runs, does not need to be usilized immediately
    
    if low is None:
        low = 0 # if low is None, then Low should be the lowest index available to be checked: 0, since counting in programming languages starts from 0
    if high is None:
        high = len(l) - 1 # if high is None, then high should be the highest index available: len(l) -1 = length of list: l minus 1

    # CHECK CONDITION FOR IF target IS NOT IN LIST  
    # if iterated properly, high should never be less than low
        # with each iteration, either 1 is subtracted from the high OR 1 is added to the low
        # if high is less than low OR low is greater than high, then all list elements have been checked without finding the target
    if high < low:
        return -1
    
    # example l = [1, 3, 5, 10, 12]   # should return 3
    #midpoint = (len(l)) // 2 # "find the midpoint of the length of list: l, then divide that value by 2 and round down" -> should approximately give the index of the midpoint 
                            # // means "floor division" -> division operator that returns the largest possible integer, rounds the answer DOWN -> integer answer will be less tha or equal to normal division result [from "https://www.educative.io/answers/floor-division"]
    midpoint = (low + high) // 2 # (low + high) is the same as previous len(l) -> (midpoint = low[number with least value] + high[number with greatest value] / 2) OR (midpoint = total length / 2)


    # CHECK IF THE CURRENT ITERATED INDEX == TARGET, divide the list in two sections based on if the selected index's value is GREATER THAN or LESS THAN the target value 
    if l[midpoint] == target: # if the midpoint of list: l is equal to the target, then return the midpoint because it is the target
        return midpoint
    elif target < l[midpoint]: # if the target's value is less than the midpoint value, divide the list in half and only search the half of the list that is greater than the previously checked index's value, find midpoint of remaining list of values and check that index's value
        return binary_search(l, target, low, midpoint-1) # when l[midpoint] is greater than Target, high = midpoint-1 -> reduces list of available numbers to check to the current low INDEX and the next INDEX that is greater than the current midpoint's INDEX
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high) # when l[midpoint] is less than Target, low = midpoint+1


########################################################################################
### SETUP OPTION 1 -> compare both search methods -> run binary_search.py
########################################################################################
# option checks to see if both functions work correctly -> both should print index: 3
#if __name__=='__main__':
#    l = [1, 3, 5, 10, 12]
#    target = 10
#    print(naive_search(l, target))
#    print(binary_search(l, target))



########################################################################################
### SETUP OPTION 2 -> requires "import random" and "import time" python modules up top
########################################################################################
    # random module used to pick random number
    # time module used to check how long it takes for each of the two search methods to reach an answer
length = 10000
# build a sorted list of length 10000
sorted_list = set()
while len(sorted_list) < length:
    # add a random integer (includes up to 3 times the length in positive and negative integers)
    sorted_list.add(random.randint(-3*length, 3*length))
sorted_list = sorted(list(sorted_list)) # make the sorted list into a sorted list and store the sorted list in variable: sorted_list

##### TIMERS for comparing search methods #####
    # Track the total amount of time it takes to search through sorted_list

##TIMER: naive_search()##
start = time.time() # time.time() -> the current time "gets the time right now"
for target in sorted_list:  # go through sorted_list and make everything the target "basically running naive_search 10000 times [because there are 10000 elements in the list]"
    naive_search(sorted_list, target)
end = time.time()
# total time for naive_search = end time - start time
    # time per iteration: total search time/length -> average time per iteration 
print("Naive search time: ", (end - start)/length, "seconds")


##TIMER: binary_search()##
start = time.time() 
for target in sorted_list:  
    binary_search(sorted_list, target)
end = time.time()
print("Binary search time: ", (end - start)/length, "seconds")



################################################################
##### RESULTS: Times after comparison run [SETUP OPTION 2] #####
################################################################

# Naive search time:  0.00018773784637451173 seconds = 187.74 microseconds
# Binary search time:  2.6608705520629885e-06 seconds = 2.6609 microseconds

# Binary search is much faster than naive search.
