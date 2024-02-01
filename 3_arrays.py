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
    array2 = ["CUM", True, []]         # <----- array with elements "CUM", True, and []
    array3 = [array0, array1, array2]   # <----- array with elements array0, array1 and array2

    print(array0)
    print(array1)
    print(array2)
    print(array3)

# Output in Terminal:
# []
# [1, 2, 3]
# ['CUM', True, []]
# [[], [1, 2, 3], ['CUM', True, []]]

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
# Note: if you use insert your a bitch. Also remember that [a:b] can be used on arrays.
def addElementAfterIndex(array, index, newElement):
    pass

########################### Grader ##########################

print()

correct = [True, True, True, True, True, True]

# Problem 1:
if returnArrayOfSize3() != None:
    if len(returnArrayOfSize3()) != 3:
        correct[0] = False
        print("Problem 1 is incorrect!")
        print("Expected: len(returnArrayOfSize3()) -> 3")
        print("Received: len(returnArrayOfSize3()) -> " + str(len(returnArrayOfSize3())))
        print()
else:
    correct[0] = False

# Problem 2:
if appendArray([1, 2, 3], 6) == None:
    correct[1] = False
elif appendArray([1, 2, 3], 6) != [1, 2, 3, 6]:
    correct[1] = False
    print("Problem 2 is incorrect!")
    print("Expected: appendArray([1, 2, 3], 6) -> [1, 2, 3, 6]")
    print("Received: appendArray([1, 2, 3], 6) -> " + str(appendArray([1, 2, 3], 6)))
    print()

# Problem 3:
prob8 = [[[1, 2, 3], 0, True], [[1, 2, 3, 4], 3, True], [[1, 2, 3, 4, 5], 5, False], [[1, 2], -1, False]]
for p in prob8:
    if inRange(p[0], p[1]) == None:
        correct[2] = False
        break
    if inRange(p[0], p[1]) != p[2]:
        correct[2] = False
        print("Problem 3 is incorrect!")
        print("Expected: inRange(" + str(p[0]) + ", " + str(p[1]) + ") -> " + str(p[2]))
        print("Received: inRange(" + str(p[0]) + ", " + str(p[1]) + ") -> " + str(inRange(p[0], p[1])))
        print()
        break

# Problem 4:
prob9 = [[[1, 2], 0, [2, 2]], [[1, 2, 5, 9], 2, [1, 2, 10, 9]]]
prob9c = [[[1, 2], 0, [2, 2]], [[1, 2, 5, 9], 2, [1, 2, 10, 9]]]
for i in range(0, len(prob9)):
    p = prob9[i]
    pc = prob9c[i]
    a = doubleAtIndex(p[0], p[1])
    if a == None:
        correct[3] = False
        break
    if a != p[2]:
        correct[3] = False
        print("Problem 4 is incorrect!")
        print("Expected: doubleAtIndex(" + str(pc[0]) + ", " + str(pc[1]) + ") -> " + str(pc[2]))
        print("Received: doubleAtIndex(" + str(pc[0]) + ", " + str(pc[1]) + ") -> " + str(a))
        print()
        break
# Problem 5:
prob10 = [[[1, 2], [1, 2, 4]], [[1, 2, 5, 9], [1, 2, 5, 9, 18]], [[1], [1, 2]]]
prob10c = [[[1, 2], [1, 2, 4]], [[1, 2, 5, 9], [1, 2, 5, 9, 18]], [[1], [1, 2]]]
for i in range(0, len(prob10)):
    p = prob10[i]
    pc = prob10c[i]
    a = appendArrayWithDoubleOfLastElement(p[0])
    if a == None:
        correct[4] = False
        break
    if a != pc[1]:
        correct[4] = False
        print("Problem 5 is incorrect!")
        print("Expected: appendArrayWithDoubleOfLastElement(" + str(pc[0]) + ") -> " + str(pc[1]))
        print("Received: appendArrayWithDoubleOfLastElement(" + str(pc[0]) + ") -> " + str(a))
        print()
        break
# Problem 6:
prob11 = [[[1, 2], 1, 20, [1, 2, 20]], 
          [[1], 0, 5, [1, 5]], 
          [[1, 2, 3, 4, 5, 6], 2, 1, [1, 2, 3, 1, 4, 5, 6]], 
          [[20, 8, 10], 2, "a", [20, 8, 10, "a"]], 
          [[5, 9, "", "12"], 1, [], [5, 9, [], "", "12"]]]

for p in prob11:
    if addElementAfterIndex(p[0], p[1], p[2]) == None:
        correct[5] = False
        break
    if addElementAfterIndex(p[0], p[1], p[2]) != p[3]:
        correct[5] = False
        print("Problem 6 is incorrect!")
        print("Expected: addElementAfterIndex(" + str(p[0]) + ", " + str(p[1]) + ", " + str(p[2]) + ") -> " + str(p[3]))
        print("Received: addElementAfterIndex(" + str(p[0]) + ", " + str(p[1]) + ", " + str(p[2]) + ") -> " + str(addElementAfterIndex(p[0], p[1], p[2])))
        print()
        break

amountCorrect = 0
for c in correct:
    if c:
        amountCorrect += 1

grade = int((amountCorrect/6)*100)

print("Grade: " + str(grade))