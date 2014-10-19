__author__ = 'cxa70'
# use provided data to find characters?
import string
import re

pattern = "[a-z]([A-Z]{3}[a-z]{1}[A-Z]{3})[a-z]"

rawDataFile = open("matchPattern.txt", "r")
rawData = ""
matches = []

for line in rawDataFile:
    match = re.findall(pattern, line)
    if match:
        matches += match

for match in matches:
    rawData += match[3]

print(matches)
print(rawData)