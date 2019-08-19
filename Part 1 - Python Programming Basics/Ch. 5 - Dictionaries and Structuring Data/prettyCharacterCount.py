# If you import the pprint module into your programs, you'll have access to the
# pprint() and pformat() functions that will "pretty print" a dictionary's values.
# This is helpful when you want a cleaner display of the items in a dictionary
# than what print() provides.

import pprint


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

# The pprint.pprint() function is especially helpful when the dictionary itself contains
# nested lists or dictionaries

# If you want to obtain the prettified text as a string value instead of displaying it
# on the screen, call pprint.pformat() instead.