# Sometimes there is a pattern that you want to match only optionally.
# That is, the regex should find a match whether or not that bit of text
# is there. The ? character flags the group that precedes it as an optional
# part of the pattern.

import re

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')

print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

# The (wo)? part of the regular expression means that the pattern wo
# is an optional group.  The regex will match text that has zero instances
# or one instance of 'wo' in it. This is why the regex matches both 
# 'Batwoman' and 'Batman'

# Using the earlier phone number example, you can make the regex look
# for phone numbers that do or do not have an area code.  

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-444-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

# You can think of the ? as saying, "Match zero or one of the groups
#  preceding this question mark" If you need to match an actual
# question mark character, escape it with \?