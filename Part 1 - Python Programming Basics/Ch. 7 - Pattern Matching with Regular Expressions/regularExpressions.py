# Regular expressions, called regexes for short, are descriptions for a pattern
# of text.  For example, a \d in a regex stands for a digit character - that is
# any single numeral 0 to 9.  The regex \d\d\d-\d\d\d-\d\d\d\d is used by Python
# to match the same text the previous isPhoneNumber() function did: a string
# of three numbers, a hypehn, three more numbers, another hyphen, and four
# numbers.  Any other string would not match the \d\d\d-\d\d\d-\d\d\d\d regex.

# But regular expressions can be much more sophisticated.  For example, adding a 3
# in curly brackets ({3}) after a pattern is like saying, "Match this pattern
# three times." So the slightly shorter regex \d{3}-\d{3}-\d{4} also matches
# the correct phone number format.

# All the regex functions in Python are in the re module. Enter the following
# into the interactive shell to import this module:
# import re

import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Remember that escape characters in Python use the backslash.  We're using a 
# raw string here by placing the 'r' before the regex object which does
# not escape the characters
