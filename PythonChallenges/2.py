__author__ = 'cxa70'
# use provided data to find characters?
import string

rawDataFile = open("rareChars.txt", "r")
rawData = ""

for line in rawDataFile:
    for char in line:
        if (string.ascii_lowercase.__contains__(char)):
            rawData += char

print(rawData)