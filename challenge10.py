"""
    Click on the picture, we can get sequence.txt:
    a = [1, 11, 21, 1211, 111221,

    Consider the hint we have -- len(a[30]),
    we are going to figure out what the 30th element of a is.

    1
    one 1 --> 11
    two 1's --> 21
    one 2 and one 1 --> 1211
    etc.

    So we can get the following algorithm to solve the problem.
    Result: 5808

    Reference:
    1. https://leetcode.com/problems/count-and-say/
"""


def transform(s):
    c = s[0]  # First char
    count = 1
    size = len(s)
    res = []

    i = 1
    while i < size:
        # Same char will increase the count
        if s[i] == c:
            count += 1

        # New char will reset the count and add a segment of string
        else:
            res.append(str(count) + c)
            c = s[i]
            count = 1
        i += 1

    res.append(str(count) + c)
    return ''.join(res)


a = "1"
N = 30

for _ in range(N):
    a = transform(a)
print(len(a))
