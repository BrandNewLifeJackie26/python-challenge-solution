"""
    Step 1:
    Inharmonious stripes in the png indicate embedded data.
    Use PIL to deal with data inside:
    https://pillow.readthedocs.io/en/stable/

    (Writing a decoding function is extremely hard, see ref:
    https://en.wikipedia.org/wiki/Portable_Network_Graphics)

    We can estimate the data in the middle of the picture,
    to be accurate, we can print the first column of data

    Step 2:
    Get data in the row

    Output:
    smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

    Step 3:
    Transform the number into chars: integrity
"""

from PIL import Image

with Image.open("oxygen.png") as im:
    width, height = im.size

    """
        Get data, each pixel represents (R, G, B, Alpha),
        organized row-wise in a single list
    """
    pix = list(im.getdata())

    """
        Print out the first col, find consecutive of (115, 115, 115, 255)
    """
    # for i in range(height):
    #     print(pix[i * width])


    """
        Find the row index of embedded data
    """
    # for i in range(height):
    #     if pix[i * width] == (115, 115, 115, 255):
    #         print(i)
    #         break

"""
    Decode data
"""
i = 43  # data row
res = []
for j in range(width):
    try:
        if j % 7 == 0:  # print out the row, and each char appears seven consecutive times
            res.append(chr(pix[i * width + j][0]))
    except ValueError:
        break
print(''.join(res))

"""
    Decode next level
"""
nums = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join([chr(n) for n in nums]))
