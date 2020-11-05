"""
    The mapping written in the paper is meant to tell you the whole mapping of all alphabets
    i.e. ABCD...
         \\\\
         CDEF...
    So try to decode the violet message and the given url.
    BTW, this encryption method is called Caesar Cipher: https://en.wikipedia.org/wiki/Caesar_cipher
"""

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "map"

"""
    Method 1: Brute Force
"""
def decode(c):
    if ord('a') <= ord(c) <= ord('z'):
        decoded_c = ord(c) + 2
        return chr(decoded_c) if decoded_c <= ord('z') else chr(decoded_c - 26)
    else:
        return c

res = [decode(c) for c in s]
res_url = [decode(c) for c in url]
print(''.join(res))
print(''.join(res_url))


"""
    Method 2: We can also make use of str.maketrans() and str.translate
"""
trans_table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
print(s.translate(trans_table))
print(url.translate(trans_table))
