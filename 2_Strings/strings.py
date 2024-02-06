########################## Strings ##########################

#----------------------# Explanation #---------------------#
# What is a string?
#    A string is a data type that is made up of a series of 
# characters. A character is anything that you can type into
# a string.


#------------------------# Example #-----------------------#

#   string = "Hello World! 123 ;: []" <--- This is a string

#   character1 = "p" <----- This is a character

#   character2 = "1" <----- This is also a character.

#   character3 = "po" <----- This is NOT a character. This is a string

#   character4 = 1 <----- This is NOT a character. This is an int

# Note: All characters are strings but not all strings are characters in python.


#----------------------# Explanation #---------------------#

# In python and many other languages, you can combine strings
# together by adding them together.

#------------------------# Example #-----------------------#
def combineStringsExample():
    A = "He"
    B = "llo"
    print(A)
    print(B)
    print(A + B)
    print(B + A)

# Output in Terminal:
# He
# llo
# Hello
# lloHe


#----------------------# Explanation #---------------------#

# Another feature of strings is that you can extract 
# specific characters from them by using "[]" with an index
# number inside indicating the position of the character
# you want.

# Note: position indexes start at 0.

#------------------------# Example #-----------------------#
def indexExample():
   string = "abcdef"

   print(string[0])
   print(string[5])

# Output in Terminal:
# a
# f

# Example Showing how string characters are indexed:

#            |         |
#   Index:   0 1 2 3 4 5
#   String: "a b c d e f"


#----------------------# Explanation #---------------------#

# In python you can get the size of a string by putting it
# in the "len" function.

#------------------------# Example #-----------------------#
def lengthExample():
   print(len("abcdef"))

# Output in Terminal:
# 6


#----------------------# Explanation #---------------------#

# In python you can get a section of a string by adding [x:y]
# after a string where "x" is the start of the section you
# want and "y" is the end of the section.

# Note: "x" is inclusive and "y" is exclusive.

#------------------------# Example #-----------------------#
def getSectionExample():
    print("BigBurger"[1:5]) # 1 is inclusive while 5 is exclusive

# Output in terminal:
# igBu

# Index view of "BigBurger":

#            [ - - ] 
# Index:   0 1 2 3 4 5 6 7 8
# String: "B i g B u r g e r"


#----------------------# Explanation #---------------------#

# In python you can use the "in" keyword to check if a string
# is inside of another string.

#------------------------# Example #-----------------------#
def containsExample():
    if "lo" in "hello":
        print(True)
        return
    print(False)

# Output in Terminal:
# True

#-------------------------# Work #-------------------------#

# Run autograder by typing 
# python3 stringsGrader.py 
# into terminal.

# Problem 1:
# Combine the first, middle and last name into one string and return it.
def getFullName(firstName, middleName, lastName):
    pass

# Problem 2:
# Combine the first and last letter of the inputed string and return it.
# If the string is empty return "" aka the empty string.
def getFirstAndLastLetterCombined(string):
    pass

# Problem 3:
# Return the section of the inputed string from a (inclusive) to b (exclusive)
def getSubstring(string, a, b):
    pass

# Problem 4:
# Return the string excluding the substring.
# EXAMPLE: getStringExcludingSubstring("BigBurger!", 1, 5) -> "Brger"
# Hint: "Brger" = "B" + "rger"
def getStringExcludingSubstring(string, a, b):
    pass

# Problem 5:
# Return True if the foodName inputed is a burger.
# EXAMPLE: Hamburger or Turkeyburger would return True. Hot dog would return False.
def isBurger(foodName):
    pass