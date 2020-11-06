"""
    The hint leads you to use urllib to iterate through all 'nothing' ids.

    Output:
    16044
    Yes. Divide by two and keep going.
    ...
    ...
    ...
    There maybe misleading numbers in the text. One example is 82683.
    Look only for the next nothing and the next nothing is 63579
    ...
    ...
    ...
    66831
    peak.html
"""


import urllib.request as req

start_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing_id = "63579"
content = ""

while True:
    with req.urlopen(start_url + nothing_id) as f:
        # We can increase the number to get larger content to avoid curtailing
        content = f.read(100).decode('utf-8')
        nothing_id = content.split(' ')[-1]
    print(nothing_id)

    # To keep notice of strange instructions, we break when encountering non-numeric output
    try:
        _ = int(nothing_id)
    except ValueError:
        print(content)
        break
