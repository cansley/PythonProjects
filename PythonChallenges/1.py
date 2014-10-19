__author__ = 'cxa70'

import string
#convert garbled text to real text
#hint: k --> m
#      o --> q
#      e --> g

garbledText = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
cleanText = ""

#having completed the challenge, use this to move to the next page
garbledText = "map"

for char in garbledText:
    if string.ascii_lowercase.__contains__(char):
        idx = string.ascii_lowercase.index(char) + 2
        if idx > len(string.ascii_lowercase) - 1:
            idx -= len(string.ascii_lowercase)

        cleanText += string.ascii_lowercase[idx]
    else:
        cleanText += char

print(cleanText)