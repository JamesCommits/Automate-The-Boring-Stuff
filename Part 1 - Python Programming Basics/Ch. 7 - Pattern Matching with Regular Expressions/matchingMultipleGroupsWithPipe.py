# The | character is called a pipe. You can use it anywhere you want to match
# one of many expressions. For example, the regular expression
# r'Batman|Tina Fey' will match either 'Batman' or 'Tina Fey'

# When both 'Batman' AND 'Tina Fey' occur in the searched string, the first occurrence
# of matching text will be returned as the Match object.

import re

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

# You can also use the pipe to match one of several patterns as part of your regex.
# For example, say you wanted to match any of the strings 'Batman', 'Batmobile',
# 'Batcopter', and 'Batbat'. Since all of these strings start with Bat, it would
# be nice if you could specify that prefix only once.  This can be done with parentheses.

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))