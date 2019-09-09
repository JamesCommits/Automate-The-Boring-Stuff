# Normally, regular expressions match text with the exact casing
# you specify.  These all match different strings for example:

import re
regex1 = re.compile('Robocop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

# But sometimes you care only about matching the letters without
# worrying whether they're uppercase or lowercase.  To make your
# regex case-insensitive, you can pass re.IGNORECASE or re.I
# as a second argument to re.compile() For example:

robocop = re.compile(r'robocop', re.I)
robocop.search('Robocop is ')