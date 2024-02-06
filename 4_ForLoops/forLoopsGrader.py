from forLoops import *
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

inputTestCases1 = [[[1, 2, 3, 4, 5]], [[5, 10, 2]], [[1]], [[]]]
expectedOutputTestCases1 = [15, 17, 1, 0]
problems[0] = bulkTest(1, sum, inputTestCases1, expectedOutputTestCases1)

inputTestCases2 = [[[5, 10, 15, 20], 10], [[4, -2, 8, 9], 9], [[9, 1, 4], 9], [[1, 2, 3, 4, 20], 10], [[], 1]]
expectedOutputTestCases2 = [1, 3, 0, -1, -1]
problems[1] = bulkTest(2, search, inputTestCases2, expectedOutputTestCases2)

inputTestCases3 = [[[1, 2, 3]], [[30, 20, 10]], [[10, -100, 5, 50]]]
expectedOutputTestCases3 = [1, 10, -100]
problems[2] = bulkTest(3, findMin, inputTestCases3, expectedOutputTestCases3) 

inputTestCases4 = [[[10, 6, 7], [10, 6, 7]], [[7, 6, 10], [10, 6, 7]], [[8, 8, 9, 10], [1]], [[], [1, 1, 9]], [[9, 1, 2, 5, 7], [9, 1, 2, 5, 7]]]
expectedOutputTestCases4 = [True, False, False, False, True]
problems[3] = bulkTest(4, areEqual, inputTestCases4, expectedOutputTestCases4) 

inputTestCases5 = [[[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [3, 2, 1]], 
                   [[1, 2, 3], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3]], 
                   [[20, 3, 5], [1, 20, 5, 6, 7, 3, 5]], [[], [1, 2, 3]],
                   [[1, 2, 3], [4, 5, 6]]]
expectedOutputTestCases5 = [True, True, True, False, True, True, False]
problems[4] = bulkTest(5, isASubsetOfB, inputTestCases5, expectedOutputTestCases5) 

inputTestCases6 = [[[5, 1, 0, 9, 10]], [[5, 4, 3, 2, 1]], [[-1, -20, 10, 7, -90, -2]], [[]], [[5, 6, 5, 8, 20, 20, 8]]]
expectedOutputTestCases6 = [[0, 1, 5, 9, 10], [1, 2, 3, 4, 5], [-90, -20, -2, -1, 7, 10], [], [5, 5, 6, 8, 8, 20, 20]]
problems[5] = bulkTest(6, sortMin2Max, inputTestCases6, expectedOutputTestCases6) 

problemsCorrect = 0
for problem in problems:
    problemsCorrect += problem

grade = int((problemsCorrect/len(problems))*100)
print("Grade: " + str(grade))