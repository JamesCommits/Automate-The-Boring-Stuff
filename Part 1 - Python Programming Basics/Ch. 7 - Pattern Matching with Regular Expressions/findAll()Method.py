# In addition to the search() method, Regex objects also have a findall() method.
# While search() will return a Match object of the first matched text in the
# searched string, the findall() method will return the strings of every
# match in the searched string. To see how search() returns a Match object
# only on the first instance of matching text:

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')

print(mo.group())

# On the other hand, findall() will not return a Match object but a list
# of strings - as long as there are no groups in the regular expression.
# Each string in the list is a piece of the searched text that matched 
# the regular expression.

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# If there ARE groups in the regular expression, then findall() will
# return a list of tuples.  Each tuple represents a found match, and
# its items are the matched strings for each group in the regex.
# To see findall() in action, enter the following:

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# To summarize what the findall() method returns:
# 1. When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d,
# the method findall() returns a list of string matches, such as 
# ['415-555-9999','212-555-0000']
#
# 2. When called on a regex that has groups such as (\d\d\d)-(\d\d\d)-(\d\d\d\d),
# the method findall() returns a list of tuples of strings (one string for each group),
# such as [('415', '555', '9999'), ('212','555','0000')]