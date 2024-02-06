########################### Arrays ##########################

#----------------------# Explanation #---------------------#
# What is an array?
#   An array is a set of data. Arrays can countain ANYTHING 
# within them. You can make an array by putting elements in
# brackets (these things: []) seperated with comas.

# Note: an element is just a thing in an array.

#------------------------# Example #-----------------------#

def creatingArray():
    array0 = []                         # <----- empty arrays.
    array1 = [1, 2, 3]                  # <----- array with elements 1, 2, and 3
    array2 = ["Hi", True, []]           # <----- array with elements "Hi", True, and []
    array3 = [array0, array1, array2]   # <----- array with elements array0, array1 and array2

    print(array0)
    print(array1)
    print(array2)
    print(array3)

# Output in Terminal:
# []
# [1, 2, 3]
# ['Hi', True, []]
# [[], [1, 2, 3], ['Hi', True, []]]

#----------------------# Explanation #---------------------#
# FUN FACT:
#   Strings are just an array of characters. Any operation that 
# you can use on a string can be used on an array.

#------------------------# Example #-----------------------#

def usingStringOperationsOnArrays():
    array = [1, 2, 3, 4, 5]

    print(array[0])         # Prints first element of array.
    print(array[0:3])       # Prints first three elements of array.
    print(len(array))       # Prints length of array
    print(array + [6, 7])   # Prints array combined with [6, 7].

    if 1 in array:          # Note: if we swapped 1 with [1] this wouldnt work since array does not have [1] as an element.
        print("True")

# Output in Terminal:
# 1
# [1, 2, 3]
# 5
# [1, 2, 3, 4, 5, 6, 7]
# True

# Index:   0  1  2  3  4
# Array:  [1, 2, 3, 4, 5]

#----------------------# Explanation #---------------------#

# You can add elements to an array in python by using the 
# .append() function after the array.

# Note: The operation [1, 2] + 3 does not work since 3 is not
# an array. However, [1, 2].append(3) would work.

#------------------------# Example #-----------------------#

def appendExample():
    array = []              # creates empty array.
    print(array)

    array.append(1)         # adds 1 to array.
    print(array)

    array.append([])        # adds [] to array.
    print(array)

    array.append("apple")   # adds "apple" to array.
    print(array)

# Output in terminal:
# []
# [1]
# [1, []]
# [1, [], 'apple']

#-------------------------# Work #-------------------------#

# Run autograder by typing 
# python3 arraysGrader.py 
# into terminal.

# Problem 1:
# Create an array of size 3 and return it. This array can contain anything you want!
def returnArrayOfSize3():
    pass

# Problem 2:
# Add element "newItem" to the array and return the array.
def appendArray(array, newItem):
    pass

# Problem 3:
# Return true if index is in the bounds of the array. Return false if it is not.
def inRange(array, index):
    pass

# Problem 4:
# Double the value of the array at index and return the array
# Example: doubleAtIndex([2, 1], 0) -> [4, 1]
def doubleAtIndex(array, index):
    pass

# Problem 5:
# Append the array with an element that is double the value of the last element in the array.
# Example: appendArrayWithDoubleOfLastElement([1, 2, 4]) -> [1, 2, 4, 8]
def appendArrayWithDoubleOfLastElement(array):
    pass

# Problem 6:
# Append the array with an element after a given index.
# Example: addElementAfterIndex([0, 1, 2], 1, 5) -> [0, 1, 5, 2]
def addElementAfterIndex(array, index, newElement):
    pass