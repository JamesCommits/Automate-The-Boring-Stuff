# If you have a group that you want to repeat a specific number of times,
# follow the group in your regex with a number in curly brackets.  For
# example, the regex (Ha){3} will match the string 'HaHaHa', but it will
# not match 'HaHa', since the latter has only two repeats of the (Ha) group.

# Instead of one number, you can specify a range by writing a minimum,
# a comma, and a maximum in between the curly brackets.  For example,
# the regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa' and 'HaHaHaHaHa'.

# You can also leave out the first or second number in the curly brackets
# to leave the minimum or maximum unbounded.  For example, (Ha){,5} will
# match zero to five instances. Curly brackets can help make your regular
# expressions shorter. These two regular expressions match identical patterns.

# (Ha){3}
# (Ha)(Ha)(Ha)

# And these two regular expressions also match identical patterns

# (Ha){3,5}
# ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

import re

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2 == None)
