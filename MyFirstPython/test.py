__author__ = 'cxa70'

import string

garbledText = "map"
cleanedText = ""
characterCode = {"k": "m",
                 "o": "q",
                 "e": "g",
                 "g": "i"}

for char in garbledText:
    if string.ascii_lowercase.__contains__(char):
        idx = string.ascii_lowercase.index(char)
        if idx == 24:
            idx = 0
        elif idx == 25:
            idx = 1
        else:
            idx += 2

        cleanedText += string.ascii_lowercase[idx]
    else:
        cleanedText += char


print(cleanedText)