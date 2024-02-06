from strings import *

####################### Grader Functions ######################

def test(problemNumber: int, func: any, inputs: list, expectedOuput: any) -> bool:
    if not callable(func):
        raise Exception(str(func) + " is not a function!")
    
    functionName: str = func.__name__

    beginningOfErrorMsg: str = functionName + "("
    for i in range(0, len(inputs)):
        if isinstance(inputs[i], str):
            beginningOfErrorMsg += "\"" + str(inputs[i]) + "\""
        elif callable(inputs[i]):
            beginningOfErrorMsg += inputs[i].__name__ + "()"
            if inputs[i]() == None:
                return False
        else:
            beginningOfErrorMsg += str(inputs[i])
        if i == len(inputs) - 1:
            break
        beginningOfErrorMsg += ", "
    beginningOfErrorMsg += str(") -> ")

    try:
        receivedOutput: any = func(*inputs)
        if receivedOutput == expectedOuput:
            return True
        elif receivedOutput == None: # Helps reduce clutter in console
            return False
        
        print("Problem " + str(problemNumber) + ":")
        
        if isinstance(expectedOuput, str):
            print("Expected: " + beginningOfErrorMsg + "\"" + expectedOuput + "\"")
        else:
            print("Expected: " + beginningOfErrorMsg + str(expectedOuput))

        if isinstance(receivedOutput, str):
            print("Received: " + beginningOfErrorMsg + "\"" + receivedOutput + "\"")
        else:
            print("Received: " + beginningOfErrorMsg + str(receivedOutput))
    except Exception as error:
        print("Problem " + str(problemNumber) + ":")
        if isinstance(expectedOuput, str):
            print("Received: " + beginningOfErrorMsg + "\"" + expectedOuput + "\"")
        else:
            print("Expected: " + beginningOfErrorMsg + str(expectedOuput))
        print("Received: " + beginningOfErrorMsg + "ERROR" + "\n" + str(error))
    return False

def bulkTest(problemNumber: int, func: any, inputTestCases: list, expectedOutputTestCases: list) -> bool:
    if len(inputTestCases) != len(expectedOutputTestCases):
        raise Exception("InputTestCases must be equal to OutputTestCases!")
    testCaseCount = len(inputTestCases)
    for i in range(0, testCaseCount):
        if not test(problemNumber, func, inputTestCases[i], expectedOutputTestCases[i]):
            return False
    return True

################### End of Grader Functions ###################

problems = [True, True, True, True, True]

# Problem 1:
inputTestCases1 = [["Bob", "Bill", "Burg"], ["Hank", "Frank", "Shrader"], ["Billie", "Bob", "Junior"]]
expectedOutputTestCases1 = ["Bob Bill Burg", "Hank Frank Shrader", "Billie Bob Junior"]
problems[0] = bulkTest(1, getFullName, inputTestCases1, expectedOutputTestCases1)

# Problem 2:
inputTestCases2 = [["Cow Milk"], ["a"], [""]]
expectedOutputTestCases2 = ["Ck", "aa", ""]
problems[1] = bulkTest(2, getFirstAndLastLetterCombined, inputTestCases2, expectedOutputTestCases2)

# Problem 3:
inputTestCases3 = [["Panda", 0, 3], ["Bear", 1, 4]]
expectedOutputTestCases3 = ["Panda"[0:3], "Bear"[1:4]]
problems[2] = bulkTest(3, getSubstring, inputTestCases3, expectedOutputTestCases3)

# Problem 4:
prob4 = [["Big Soup Man", 4, 9, "Big Man"], ["Bear Man", 0, 5, "Man"], ["Soda Bucket", 4, 11, "Soda"]]
inputTestCases4 = [["Big Soup Man", 4, 9], ["Bear Man", 0, 5], ["Soda Bucket", 4, 11]]
expectedOutputTestCases4 = ["Big Man", "Man", "Soda"]
problems[3] = bulkTest(4, getStringExcludingSubstring, inputTestCases4, expectedOutputTestCases4)

# Problem 5:
inputTestCases5 = [["Turkeyburger"], ["Hamburger"], ["Cheeseburger"], ["Hot Dog"], ["Slop Bucket"], ["Burrito"]]
expectedOutputTestCases5 = [True, True, True, False, False, False]
problems[4] = bulkTest(5, isBurger, inputTestCases5, expectedOutputTestCases5)

problemsCorrect = 0
for problem in problems:
    problemsCorrect += problem

grade = int((problemsCorrect/len(problems))*100)
print("Grade: " + str(grade))