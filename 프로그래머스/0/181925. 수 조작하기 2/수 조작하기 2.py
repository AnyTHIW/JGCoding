def solution(numLog):
    dictionary = {1:"w", -1:"s", 10:"d", -10:"a"}
    recoveredString = ""
    for i in range(1, len(numLog)):
        CharToFind = numLog[i] - numLog[i-1]
        recoveredString += dictionary[CharToFind]
    return recoveredString