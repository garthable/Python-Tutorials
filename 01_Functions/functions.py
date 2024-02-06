########################## Functions #########################

#-----------------------# Explanation #----------------------#
#   A function is a way to save time in coding. 
# They package a series of instructions into a package that 
# can be reused and executed throughout your code.

# How do they work?
#   In any programming language a function can take in a 
# series of inputs (called parameters), preform instructions
# that can use those inputs and can return an output.

# How are they defined?
#   In Python a function is defined by typing: 
# "def <NAME>(<PARAMETERA>, <PARAMETERB>):" where name is the
# name, and parameterA and parameterB are place holds for 
# parameters that may or may not exist. Within the function
# you can add "return" to end the function and send data out
# of it.

#-------------------------# Example #------------------------#

# This function takes in "a" as a parameter
def exampleFunction1(a):
    return a*2 # returns a*2

# n = 5
# nDoubled = exampleFunction1(n)
# 
# Value of n: 5
# Value of nDoubled: 10 

# This function takes in "a" and "b" as parameters.
def exampleFunction2(a, b):
    c = a+b
    if c > 5:
        return c*a # if c is greater than 5 return c*a
    elif c == 5:
        return a # if c is equal to 5 return a
    # if neither of these are true the function will return nothing.

# Examples of how code could operate within function:

# Case a + b > 5:
# foo = 2
# bar = 5
# baz = exampleFunction2(foo, bar)

# Value of foo: 2
# Value of bar: 5
# Value of baz: 14

# Case a + b == 5:
# x = 2
# y = 3
# z = exampleFunction2(x, y)

# Value of x: 2
# Value of y: 3
# Value of z: 2

# Case a + b < 5:
# i = 1
# j = 1
# k = exampleFunction2(i, j)

# Value of i: 1
# Value of j: 1
# Value of k: null (null means nothing in code)

#--------------------------# Work #--------------------------#

# Run autograder by typing 
# python3 functionsGrader.py 
# into terminal.

# PROBLEM 1
# This function should return 1.
def return1():
    pass

# PROBLEM 2
# This function should return the sum of two parameters passed into it.
def sum(a, b):
    pass

# PROBLEM 3
# This function should return True if the value is between minInclusive and maxExclusive or equal to minInclusive
# Note: Exclusive means that it excludes the value listed, Inclusive means that it includes the value listed.
def inRange(value, minInclusive, maxExclusive):
    pass

# PROBLEM 4
# This function should clamp the value between minInclusive and maxInclusive
# Note: the max is not exclusive
def clamp(value, minInclusive, maxInclusive):
    pass

# PROBLEM 5
# This function should return True of the guessedValue is equal to the correctValue.
def guessedCorrectly(guessedValue, correctValue):
    pass