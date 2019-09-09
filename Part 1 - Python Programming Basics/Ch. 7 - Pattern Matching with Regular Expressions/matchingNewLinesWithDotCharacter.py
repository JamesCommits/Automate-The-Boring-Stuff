# The dot-star will match everything except a newline.  By passing re.DOTALL
# as the second argument to re.compile(), you can make the dot character match
# all characters, including the newline character. For example:

import re

noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
# Prints everything on the first line, but stops because dot-star cannot print new lines.

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
# newlineRegex has the re.DOTALL passed to re.compile(), matching everything. This is why
# the newlineRegex.search() call matches the full string, including its newline characters.