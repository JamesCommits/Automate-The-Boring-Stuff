# Sometimes you will want to match everything and anything.  For example,
# say you want to match the string 'First Name: ', followed by any and all
# text, followed by 'Last Name: ', and then followed by anything again.  You
# can use the dot-star (.*) to stand in for that 'anything.' Remember that the
# dot character means 'any single character except the newline,' and the star
# character means 'zero or more of the preceding character.' For example:

import re

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: James Last Name: Commits')
print(mo.group(1))
print(mo.group(2))

# The dot-star uses the greedy mode: It will always try to match as much text
# as possible. To match any and all text in a nongreedy fashion, use the dot,
# star, and question mark (.*?).  Like with curly brackets, the question mark
# tells Python to match in a nongreedy way. For example:

nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# In the non-greedy version of the regex, Python matches the shortest possible
# string: '<To serve man>.' In the greedy version, Python matches the longest
# possible string: '<To serve man> for dinner.>'