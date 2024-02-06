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