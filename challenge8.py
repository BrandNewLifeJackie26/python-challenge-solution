"""
    Hint:
    The picture leads us to think of bee/ insect.
    So we can actually get hints from different urls.
    insect.html -> BE more specific.
    bee.html -> and she is BUSY.
    busy.html -> all bees sound busy too. -> bz2

    So we will use bz2 to inflate (hinted by alert) u(ser)n(ame) and p(ass)w(ord) provided in page source.

    username: huge
    password: file


    Reference:
    1. PIL: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html#module-PIL.ImageDraw (We can use this to draw the mapping area)
    2. bz2: https://docs.python.org/3/library/bz2.html
    3. html <map>: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map
"""

import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print(bz2.decompress(un))
print(bz2.decompress(pw))
