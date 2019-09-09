# The . (or dot) character in a regular expression is called a wildcard
# and will match any character except for a newline.  For example:

import re

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# Remember that the dot character will match just one character, which
# is why the match for the text 'flat' in the previous example matched
# only 'lat'.  To match an actual dot, escape the dot with a backslash: \..

