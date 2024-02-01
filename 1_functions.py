#Explanations of functions:
# A function (Typed as "def" in python and "func" in GDScript) is a way to save time and memory in coding. 
#They package a series of instructions into a package that can be reused and executed throughout your code.

#HOW DO THEY WORK?
#In any programming language a function can take in a series of inputs (called parameters), preform instructions
#that can use those inputs and can return an output.

#Whenever a function is called the program will pause the code from the scope(place where code is) that the 
#function was called from and begin running that function. When the code reaches the end of the function or 
#hits a "return" instruction the code will exit out of the function and resume running the prior scope again.

#Theres more to functions but tooooo many words.

#Examples:

################################################################################

#This function takes in "a" as a parameter
def exampleFunction1(a):
    return a*2 #returns a*2

# n = 5
# nDoubled = exampleFunction1(n)
# 
# Value of n: 5
# Value of nDoubled: 10 

################################################################################

#This function takes in "a" and "b" as parameters.
def exampleFunction2(a, b):
    c = a+b
    if c > 5:
        return c*a #if c is greater than 5 return c*a
    elif c == 5:
        return a #if c is equal to 5 return a
    #if neither of these are true the function will return nothing.

# Case c > 5:
# pee = 2
# poo = 5
# icky = exampleFunction2(pee, poo)

# Value of pee: 2
# Value of poo: 5
# Value of icky: 14

# Case c == 5:
# x = 2
# y = 3
# z = exampleFunction2(x, y)

#Value of x: 2
#Value of y: 3
#Value of z: 2

# Case c < 5:
# i = 1
# j = 1
# k = exampleFunction2(i, j)

#Value of i: 1
#Value of j: 1
#Value of k: null (null means nothing in code)

################################################################################

#Work:
#Auto Graded Work:

#This function should return 1.
def return1():
    return 1

#This function should return the sum of two parameters passed into it.
def sum(a, b):
    return a + b

#This function should return True if the value is between minInclusive and maxExclusive or equal to minInclusive
#Note: Exclusive means that it excludes the value listed, Inclusive means that it includes the value listed.
def inRange(value, minInclusive, maxExclusive):
    if value < minInclusive:
        return False
    elif value >= maxExclusive:
        return False
    return True

#This function should clamp the value between minInclusive and maxInclusive
#Note: the max is not exclusive
def clamp(value, minInclusive, maxInclusive):
    if value < minInclusive:
        value = minInclusive
    elif value > maxInclusive:
        value = maxInclusive
    return value


#This function should return True of the guessedValue is equal to the correctValue.
def guessedCorrectly(guessedValue, correctValue):
    if guessedValue == correctValue:
        return True
    return False

#Grading

correct = [True, True, True, True, True]

if return1() != 1:
    correct[0] = False
    print("Problem 1 Incorrect! return1() should return 1.")

for i in range(0, 20):
    j = (i*2)%7
    if i+j != sum(i, j):
        correct[1] = False
        print("Problem 2 Incorrect! sum(" + str(i) + ", " + str(j) + ") should return " + str(i+j) + " instead of " + str(sum(i, j)))
        break
            

trueVals = [[9, 5, 10], [1, 1, 2], [4, 1, 5], [2, 2, 8]]
falseVals = [[0, 5, 10], [2, 1, 2], [5, 1, 5], [-1, 2, 8]]

for a in trueVals:
    if not inRange(a[0], a[1], a[2]):
        correct[2] = False
        print("Problem 3 Incorrect! " + str(a[0]) + " is in the range of " + str(a[1]) + " - " + str(a[2]))
        break
if correct[2]:
    for a in falseVals:
        if inRange(a[0], a[1], a[2]):
            correct[2] = False
            print("Problem 3 Incorrect! " + str(a[0]) + " is in not the range of " + str(a[1]) + "-" + str(a[2]))
            break

vals = [[0, 5, 10, 5], [1, 1, 2, 1], [4, 1, 5, 4], [10, 2, 8, 8], [10, 8, 10, 10]]

for a in vals:
    if clamp(a[0], a[1], a[2]) != a[3]:
        correct[3] = False
        print("Problem 4 Incorrect! " + str(a[0]) + " clamped between " + str(a[1]) + "-" + str(a[2]) + " is " + str(a[3]) + " not " + str(clamp(a[0], a[1], a[2]))) 
        break

for a in range(0, 400):
    i = a % 20
    j = a / 20
    if (i == j) != guessedCorrectly(i, j):
        correct[4] = False
        print("Problem 5 Incorrect! FOOL FOOL IDIOT")
        break


grade = 0
for i in range(0, 5):
    if correct[i]:
        grade += 20

print("Grade: " + str(grade))