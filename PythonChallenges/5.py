__author__ = 'cxa70'

import pickle
pk = pickle.Unpickler(open("banner.p", "rb"))

wtfAmI = pk.load()
stringThing = ""
for thing in wtfAmI:
    for subThing in thing:
        stringThing += subThing[0]*subThing[1]

    stringThing += "\n"

print(stringThing)