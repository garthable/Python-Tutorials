########################## For Loops #########################

#-----------------------# Explanation #----------------------#
# What are loops?
#   Loops are an instruction that iterate over code.

#-------------------------# Example #------------------------#
# Note: This is pseudocode and will not work in Python.

# print("Outside Loop (above)")
# LOOP 3 TIMES:
#   print("Inside Loop 1")
#   print("Inside Loop 02")
# print("Outside Loop (below)")

# Output in Terminal:
#   Outside Loop (above)
#   Inside Loop 1
#   Inside Loop 02
#   Inside Loop 1
#   Inside Loop 02
#   Inside Loop 1
#   Inside Loop 02
#   Outside Loop (below)

#-----------------------# Explanation #----------------------#
# What are for loops?
#   For loops are a type of loop that iterate through all 
# elements in a given array. For loops allow you to read each 
# element in an array.

# Loops are formatted like this:
#   for variable in array:

# "for" and "in" are both part of the format and do not change.

# "variable" is the name of the variable that will copy each
# element of the array.

# "array" is either the name of a preexisting array or is an
# array that has been directly typed in.

#-------------------------# Example #------------------------#

# Pseudocode of how for how loop works:
# def forLoopExample1():
#     array = [1, 2, 3]               <-- Predefined array
#     print("Outside Loop (above)")
#     i = 0                           <-- Initializes iterator value
#     LOOP len(array) TIMES:          <-- Loops length of array times (or 3)
#         variable = array[i]         <-- Copies value at index i to variable
#         print(variable)
#         i += 1                      <-- Increases iterator
#     print("Outside Loop (below)")

# Same as pseudocode but now uses actual code:
def forLoopExample1():
    array = [1, 2, 3]
    print("Outside Loop (above)")
    for variable in array:
        print(variable)
    print("Outside Loop (below)")

# Output in terminal from forLoopExample1:
#   Outside Loop (above)
#   1
#   2
#   3
#   Outside Loop (below)
    
def forLoopExample2():
    array = [1, 2, 3]
    print(array)
    for variable in array:
        variable = 2   # Remember i is only a copy of the array value, modifying it dosent change the array.
        print(variable)
    print(array)

# Output in terminal from forLoopExample2:
#   [1, 2, 3]
#   2
#   2
#   2
#   [1, 2, 3]

def forLoopExample3():
    product = 1
    array = [2, 3, 4]
    print(product)
    for n in array:
        product *= n
        print(product)

# Output in terminal from forLoopExample3:
#   1
#   2
#   6
#   24
        
#-----------------------# Explanation #----------------------#
# range(startInclusive, stopExclusive, step):
#   range is a function in Python that allows you to have a 
# variable in a for loop range from startInclusive up until 
# stopExclusive. Step controls the incrememnt that it grows at.
        
# TIPS: range(a) will default to range(0, a, 1)
#       range(a, b) will default to range(a, b, 1)
#-------------------------# Example #------------------------#
        
def rangeExample1():
    for i in range(0, 5, 1):
        print(i)

# Output in terminal:
#   0
#   1
#   2
#   3
#   4

def rangeExample2():
    array = [1, 2, 3, 4, 5, 6]
    for i in range(3, len(array), 1):
        array[i] *= 2  # <-- modifies actual array
        print(i)
    print(array)

# Output in terminal:
#   3
#   4
#   5
#   [1, 2, 3, 8, 10, 12]
        
def rangeExample3():
    array1 = [2, 8, 1, 3, 60]
    array2 = [3, 4, 1, 2, 10]
    array3 = []
    for i in range(0, len(array1), 2):
        array3.append(array1[i] + array2[i])
        print(i)
    print(array3)

# Output in terminal:
#   0
#   2
#   4
#   [5, 2, 70]
        
#-----------------------# Explanation #----------------------#
# continue:
#   continue forces the for loop to go to the next iteration.

#-------------------------# Example #------------------------#

def continueExample():
    array = [1, 2, 3]
    for n in array:
        print("Start " + str(n))
        if n == 2:
            print("Skipped " + str(n))
            continue
        print("End " + str(n))

# Output in terminal:
#   Start 1
#   End 1
#   Start 2
#   Skipped 2
#   Start 3
#   End 3

#-----------------------# Explanation #----------------------#
# break:
#   break forces the for loop to end.

#-------------------------# Example #------------------------#
def breakExample():
    array = [1, 2, 3]
    print("Start of Loop")
    for n in array:
        print("Start " + str(n))
        if n == 2:
            print("Terminated at " + str(n))
            break
        print("End " + str(n))
    print("End of Loop")

# Output in terminal:
#   Start of Loop
#   Start 1
#   End 1
#   Start 2
#   Terminated at 2
#   End of Loop

#--------------------------# Work #--------------------------#
    
# Run autograder by typing 
# python3 forLoopsGrader.py
# into terminal.
    
# Problem 1
# Given an array of numbers return the result of all of them
# added together.
def sum(array):
    pass

# Problem 2
# Return the index of the value in the array.
# Example: search([5, 9, 3], 3) -> 2
# If the value is not present in the array return -1.
def search(array, value):
    pass

# Problem 3
# Return the smallest element in the array.
# Assume the array is never empty
def findMin(array):
    pass

# Problem 4
# Return true if arrayA and arrayB are equal, return false otherwise.
# RESTRICTION: Cannot do return arrayA == arrayB, you must use for loops!
def areEqual(arrayA, arrayB):
    pass

# Problem 5
# Return True if all of arrayA's values can be found in arrayB,
# return False if they cant be.
# Assume there are no repeats in arrays given.
def isASubsetOfB(arrayA, arrayB):
    pass


# Problem 6
# Return the given array sorted from min to max.
# Tips: You can remove elements from an array via array.remove(element)
#       You can use other functions from this assignment
#       If you're having trouble with the logic of this problem it can be helpful to sort a set of numbers on paper
#       and try to figure out how you sort things.
def sortMin2Max(array):
    pass