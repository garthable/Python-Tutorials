from functions import *

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

def bulkTest(problemNumber: int, func: any, inputTestCases: list, expectedOutputTestCases: list) -> bool:
    if len(inputTestCases) != len(expectedOutputTestCases):
        raise Exception("InputTestCases must be equal to OutputTestCases!")
    for i in range(0, len(inputTestCases)):
        if not test(problemNumber, func, inputTestCases[i], expectedOutputTestCases[i]):
            return False
    return True
    
problems = [True, True, True, True, True]

# Problem 1
problems[0] = test(1, return1, [], 1)

# Problem 2
for i in range(0, 20): 
    j = (i*2)%7
    problems[1] = test(2, sum, [i, j], i+j)
    if not problems[1]:
        break

# Problem 3
inputTestCases3 = [[9, 5, 10], [1, 1, 2], [4, 1, 5], [2, 2, 8], [0, 5, 10], [2, 1, 2], [5, 1, 5], [-1, 2, 8]]
expectedOutputTestCases3 = [True, True, True, True, False, False, False, False]
problems[2] = bulkTest(3, inRange, inputTestCases3, expectedOutputTestCases3)

# Problem 4
inputTestCases4 = [[0, 5, 10], [1, 1, 2], [4, 1, 5], [10, 2, 8], [10, 8, 10]]
expectedOutputTestCases4 = [5, 1, 4, 8, 10]
problems[3] = bulkTest(4, clamp, inputTestCases4, expectedOutputTestCases4)

# Problem 5
for i in range(0, 400):
    x = int(i % 20)
    y = int(i / 20)
    problems[4] = test(5, guessedCorrectly, [x, y], x == y)
    if not problems[4]:
        break

problemsCorrect = 0
for problem in problems:
    problemsCorrect += problem

grade = int((problemsCorrect/len(problems))*100)
print("Grade: " + str(grade))