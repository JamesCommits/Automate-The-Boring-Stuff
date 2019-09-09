# There are times when you want to match a set of characters but the shorthand
# character classes (\d, \w, \s, and so on) are too broad.  You can define
# your own character class using square brackets.  For example, the
# character class [aeiouAEIOU] will match any vowel, both lowercase
# and uppercase.

import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby poop. BABY POOP.'))

# You can also include ranges of letters or numbers by using a hyphen.
# For example, the character class [a-zA-Z0-9] will match all
# lowercase letters, uppercase letters, and numbers

# By placing a caret character (^) just after the character class's 
# opening bracket, you can make a negative character class.
# A negative character class will match all the characters that
# are NOT in the character class. For example:

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby poop.  BABY POOP.'))