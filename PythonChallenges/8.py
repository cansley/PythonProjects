__author__ = 'cxa70'

import bz2

# bzip extract these values
username = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
password = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

u = bz2.decompress(username).decode('utf-8')
p = bz2.decompress(password).decode('utf-8')

print(u)
print(p)