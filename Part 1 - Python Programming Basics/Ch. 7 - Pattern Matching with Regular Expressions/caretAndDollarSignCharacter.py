# You can also use the caret symbol (^) at the start of a regex to
# indicate that a match must occur at the beginning of the searched text.
# Likewise, you can put a dollar sign ($) at the end of a regex to indicate
# the string must end with this regex pattern.  And you can use the ^ and the $
# together to indicate that the entire string must match the regex-- that is,
# it's not enough for a match to be made on some subset of the string.

# For example, the r'^Hello' regular expression string matches strings
# that begin with 'Hello'. For example:

import re

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!'))
print(beginsWithHello.search('He said hello') == None) 

# The r'\d$' regular expression string matches strings that end with a 
# numeric character from 0 to 9. For example:

endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two') == None)

# The r'^\d+$' regular expression string matches strings that both
# begin and end with one or more numeric characters. For example:

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('1234   567890') == None)

# The last two search() calls in the previous example demonstate
# how the entire string must match the regex if ^ and $ are used.

# I always confuse the meanings of these two symbols, so I use the 
# mnemonic 'Carrots cost dollars' to remind myself that the caret comes
# first and the dollar sign comes last.