"""
    NOTICE: unzip channel.zip to folder channel before running the script.
    Step 1:
    The hint leads us to change .html to .zip to get the zip.

    Step 2:
    Unzip the zip and read readme.txt.
    We should use file reader to trace the linked list of txt files.
    We find "Collect the comments" in 46145.txt.

    Step 3:
    Use zipfile.ZipFIle.getinfo(path).comment to get comment of each file.
    https://docs.python.org/3.6/library/zipfile.html?highlight=zipfile#zipinfo-objects

    Step 4:
    Print all comments out.
    Notice: comments are in format of bytes objects (which are essentially byte arrays)
    https://docs.python.org/3.6/library/stdtypes.html#bytes

    Output:
    ****************************************************************
    ****************************************************************
    **                                                            **
    **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
    **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
    **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
    **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
    **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
    **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
    **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
    **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
    **                                                            **
    ****************************************************************
     **************************************************************

    Step 5:
    We are not using HOCKEY but the letter comprising it -- OXYGEN.
"""

import zipfile

base = 'channel/'
nothing_id = '90052'
archive = zipfile.ZipFile('channel.zip', 'r')
res = []

while True:
    # Get character from comment
    res.append(chr(archive.getinfo(nothing_id + '.txt').comment[0]))

    # We can also use archive.open() to create stream, but it returns a byte stream,
    # which is harder to operate on
    with open(base + nothing_id + '.txt') as f:
        content = f.read()
        nothing_id = content.split(' ')[-1]  # Get the next nothing id

    # Break when reach the end
    try:
        _ = int(nothing_id)
    except ValueError:
        break

print(''.join(res))
