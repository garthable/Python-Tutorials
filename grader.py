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