__author__ = 'cxa70'

import urllib.request as req

rootUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "82682"
isEnd = False
http = req.urlopen(rootUrl + nothing).read().decode("utf-8")

while not isEnd:
    print(http)
    if http.__contains__('and the next nothing is'):
        nothing = http[http.index('and the next nothing is ')+24:]
    elif http.__contains__('Yes. Divide by two and keep going.'):
        value = int(nothing)
        value /= 2
        nothing = str(value)
    else:
        isEnd = True
        break

    http = req.urlopen(rootUrl + nothing).read().decode("utf-8")