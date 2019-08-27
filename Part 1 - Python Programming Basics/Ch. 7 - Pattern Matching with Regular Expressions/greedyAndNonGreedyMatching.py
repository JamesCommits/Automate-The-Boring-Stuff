# Since (Ha){3,5} can match three, four, or five instances of Ha
# in the string 'HaHaHaHaHa', you may wonder why the Match object's call
# to group() in the previous curly bracket example returns 'HaHaHaHaHa'
# instead of the shorter possibilites. After all, 'HaHaHaHa' and 'HaHaHaHaHa'
# are also valid matches of the regular expression (Ha){3,5}

# Python's regular expressions are greedy by default, which means that
# in ambiguous situations they will match the longest string possible.
# The non-greedy version of the curly brackets, which matches the 
# shortest string possible, has the closing curly bracket followed
# by a question mark.

import re

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# Note that the question mark can have two meanings in regular expressions:
# declaring a nongreedy match or flagging an optional group.
# These meanings are entirely unrelated.