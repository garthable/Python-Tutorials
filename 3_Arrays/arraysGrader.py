from arrays import *

####################### Grader Functions ######################

def test(problemNumber: int, func: any, inputs: list, expectedOuput: any) -> bool:
    if not callable(func):
        raise Exception(str(func) + " is not a function!")
    functionName: str = func.__name__

    functionInputString: str = functionName + "("
    for i in range(0, len(inputs)):
        if isinstance(inputs[i], str):
            functionInputString += "\"" + str(inputs[i]) + "\""
        elif callable(inputs[i]):
            functionInputString += inputs[i].__name__ + "()"
            if inputs[i]() == None:
                return False
            inputs[i] = inputs[i]()
        else:
            functionInputString += str(inputs[i])
        if i == len(inputs) - 1:
            break
        functionInputString += ", "
    functionInputString += str(") -> ")

    try:
        receivedOutput: any = func(*inputs)
        if receivedOutput == expectedOuput:
            return True
        elif receivedOutput == None: # Helps reduce clutter in console
            return False
        print("Problem " + str(problemNumber) + ":")
        
        if isinstance(expectedOuput, str):
            print("Expected: " + functionInputString + "\"" + str(expectedOuput) + "\"")
        else:
            print("Expected: " + functionInputString + str(expectedOuput))

        if isinstance(receivedOutput, str):
            print("Received: " + functionInputString + "\"" + str(receivedOutput) + "\"")
        else:
            print("Received: " + functionInputString + str(receivedOutput))
        return False
    except Exception as error:
        print("Problem " + str(problemNumber) + ":")
        if isinstance(expectedOuput, str):
            print("Received: " + functionInputString + "\"" + str(expectedOuput) + "\"")
        else:
            print("Expected: " + functionInputString + str(expectedOuput))
        print("Received: " + functionInputString + "ERROR" + "\n" + str(error))
        return False

def bulkTest(problemNumber: int, func: any, inputTestCases: list, expectedOutputTestCases: list) -> bool:
    if len(inputTestCases) != len(expectedOutputTestCases):
        raise Exception("InputTestCases must be equal to OutputTestCases!")
    for i in range(0, len(inputTestCases)):
        if not test(problemNumber, func, inputTestCases[i], expectedOutputTestCases[i]):
            return False
    return True

problems = [True, True, True, True, True, True]

# Problem 1:
problems[0] = test(1, len, [returnArrayOfSize3], 3)

# Problem 2:
inputTestCases2 = [[[1, 2, 3], 6], [[0, 3, 4], 3]]
expectedOutputTestCases2 = [[1, 2, 3, 6], [0, 3, 4, 3]]
problems[1] = bulkTest(2, appendArray, inputTestCases2, expectedOutputTestCases2)

# Problem 3:
inputTestCases3 = [[[1, 2, 3], 0], [[1, 2, 3, 4], 3], [[1, 2, 3, 4, 5], 5], [[1, 2], -1]]
expectedOutputTestCases3 = [True, True, False, False]
problems[2] = bulkTest(3, inRange, inputTestCases3, expectedOutputTestCases3)

# Problem 4:
inputTestCases4 = [[[1, 2, 3], 0], [[5, 10, 2], 2]]
expectedOutputTestCases4 = [[2, 2, 3], [5, 10, 4]]
problems[3] = bulkTest(4, doubleAtIndex, inputTestCases4, expectedOutputTestCases4)

# Problem 5:
inputTestCases5 = [[[1, 2, 3]], [[9, 8, 4]], [[1]]]
expectedOutputTestCases5 = [[1, 2, 3, 6], [9, 8, 4, 8], [1, 2]]
problems[4] = bulkTest(5, appendArrayWithDoubleOfLastElement, inputTestCases5, expectedOutputTestCases5)
    
# Problem 6:
inputTestCases6 = [[[1, 3, 4, 5], 0, 2], [[5, 2, 10, 4], 3, 9], [[2, 20, 3, 1], 1, 10]]
expectedOutputTestCases6 = [[1, 2, 3, 4, 5], [5, 2, 10, 4, 9], [2, 20, 10, 3, 1]]
problems[5] = bulkTest(6, addElementAfterIndex, inputTestCases6, expectedOutputTestCases6)

problemsCorrect = 0
for problem in problems:
    problemsCorrect += problem

grade = int((problemsCorrect/len(problems))*100)
print("Grade: " + str(grade))