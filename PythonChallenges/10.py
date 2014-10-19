__author__ = 'cxa70'

import string

a = [1, 11, 21, 1211, 111221, ]  # Dafuq does this even mean?
# after the first value, the number represents a description of the value before it.
# example: 1 = one 1 or 11. 11 = two 1 or 21, 21 = one 2 one 1 or 1211, etc.
def transformCharacterCount(char, count):
    assert isinstance(char, str)
    return str(count)+str(char)


testValue = "1"
masterList = [testValue, ]

runCount = 0

while runCount <= 30:
    evalChar = ""
    outputValue = ""
    charCount = 0
    for char in testValue:
        if evalChar == "":
            evalChar = char

        if evalChar == char:
            charCount += 1
        else:
            outputValue += transformCharacterCount(evalChar, charCount)
            evalChar = char
            charCount = 1

    outputValue += transformCharacterCount(evalChar, charCount)
    testValue = outputValue
    masterList.append(testValue)
    runCount += 1

print(len(masterList[30]))

