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

# Note: All characters are strings but not all strings are characters.


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
        print("True")
        return
    print("False")

# Output in Terminal:
# True

#-------------------------# Work #-------------------------#

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

########################### Grader ##########################

print()

correct = [True, True, True, True, True]

# Problem 1:
if getFullName("Dalton", "John", "Prokosch") == None:
    correct[0] = False
elif getFullName("Dalton", "John", "Prokosch") != "Dalton John Prokosch":
    correct[0] = False
    print("Problem 1 is incorrect!")
    print("Expected: getFullName(\"Dalton\", \"John\", \"Prokosch\") -> \"Dalton John Prokosch\"")
    print("Received: getFullName(\"Dalton\", \"John\", \"Prokosch\") -> \"" + str(getFullName("Dalton", "John", "Prokosch")) + "\"")
    print()

# Problem 2:
prob2 = [["Cow Milk", "Ck"], ["a", "aa"], ["", ""]]
for p in prob2:
    a = getFirstAndLastLetterCombined(p[0])
    if a == None:
        correct[1] = False
        break
    if a != p[1]:
        correct[1] = False
        print("Problem 2 is incorrect!")
        print("Expected: getFirstAndLastLetterCombined(\"" + p[0] + "\") -> \"" + p[1] + "\"")
        print("Received: getFirstAndLastLetterCombined(\"" + p[0] + "\") -> \"" + a + "\"")
        print()
        break

# Problem 3:
prob3 = [["Panda", 0, 3], ["Bear", 1, 4]]
for p in prob3:
    a = getSubstring(p[0], p[1], p[2])
    if a == None:
        correct[2] = False
        break
    if a != p[0][p[1]:p[2]]:
        correct[2] = False
        print("Problem 3 is incorrect!")
        print("Expected: getSubstring(\"" + str(p[0]) + "\", " + str(p[1]) + ", " + str(p[2]) + ") -> \"" + p[0][p[1]:p[2]] + "\"")
        print("Received: getSubstring(\"" + str(p[0]) + "\", " + str(p[1]) + ", " + str(p[2]) + ") -> \"" + str(a) + "\"")
        print()
        break

# Problem 4:
prob4 = [["Big Soup Man", 4, 9, "Big Man"], ["Bear Man", 0, 5, "Man"], ["Soda Bucket", 4, 11, "Soda"]]
for p in prob4:
    a = getStringExcludingSubstring(p[0], p[1], p[2])
    if a == None:
        correct[3] = False
        break
    if a != p[3]:
        correct[3] = False
        print("Problem 4 is incorrect!")
        print("Expected: getStringExcludingSubstring(\"" + str(p[0]) + "\", " + str(p[1]) + ", " + str(p[2]) + ") -> \"" + p[3] + "\"")
        print("Received: getStringExcludingSubstring(\"" + str(p[0]) + "\", " + str(p[1]) + ", " + str(p[2]) + ") -> \"" + str(a) + "\"")
        print()
        break

# Problem 5:
prob5 = [["Turkeyburger", True], ["Hamburger", True], ["Cheeseburger", True], ["Hot Dog", False], ["Slop Bucket", False], ["Burrito", False]]
for p in prob5:
    if isBurger(p[0]) == None:
        correct[4] = False
        break
    if isBurger(p[0]) != p[1]:
        correct[4] = False
        print("Problem 5 is incorrect!")
        print("Expected: isBurger(\"" + str(p[0]) + "\") -> " + str(p[1]))
        print("Received: isBurger(\"" + str(p[0]) + "\") -> " + str(isBurger(p[0])))
        print()
        break

amountCorrect = 0
for c in correct:
    if c:
        amountCorrect += 1

grade = int((amountCorrect/5)*100)

print("Grade: " + str(grade))