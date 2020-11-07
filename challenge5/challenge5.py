"""
    Step 1:
    Peak hell --> Pickle
    https://docs.python.org/3/library/pickle.html

    Step 2:
    Find hidden file banner.p in source code,
    unpickle and print them out

                  #####                                                                      #####
                   ####                                                                       ####
                   ####                                                                       ####
                   ####                                                                       ####
                   ####                                                                       ####
                   ####                                                                       ####
                   ####                                                                       ####
                   ####                                                                       ####
          ###      ####   ###         ###       #####   ###    #####   ###          ###       ####
       ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     ####
      ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   ####
     ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  ####
     ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  ####
    ####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  ####
    ####           ####     ####   ##########    ####     ####  ####     #### ##############  ####
    ####           ####     ####  ###    ####    ####     ####  ####     #### ####            ####
    ####           ####     #### ####     ###    ####     ####  ####     #### ####            ####
     ###           ####     #### ####     ###    ####     ####  ####     ####  ###            ####
      ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   ####
       ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    ####
          ###     ######    #####    ##    #### ######    ###########    #####      ###      ######
"""

import pickle

# By default, file will be read in as string stream, so change it to byte-object file stream
with open("banner.p", "rb") as f:
    res = pickle.load(f)

# Notice that the ' ' and '#' appear alternately and every line has same amount of chars
# So try to draw it out line by line
for line in res:
    print(''.join([c * n for c, n in line]))
