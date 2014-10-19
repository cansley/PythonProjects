__author__ = 'cxa70'

import zipfile

zf = zipfile.ZipFile('channel.zip')

targetFileName = "readme.txt"
isEnd = False
masterComment = ""

while not isEnd:
    content = zf.read(targetFileName).decode("utf-8")
    masterComment += zf.getinfo(targetFileName).comment.decode('utf-8')
    if content.__contains__("start from"):
        startIdx = content.index("start from") + 11
        endIdx = content.index("\n", startIdx)
        targetFileName = content[startIdx:endIdx] + ".txt"
    elif content.__contains__("Next nothing is"):
        startIdx = content.index("Next nothing is") + 16
        targetFileName = content[startIdx:] + ".txt"
    else:
        isEnd = True

print(masterComment)