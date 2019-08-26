# Say you want to separate the area code from the rest of the phone number.  
# Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d)-(\d\d\d\d)
# Then you can use the group() match object method to grab the matching
# text from just one group.  

# The first set of parentheses in a regex string will be group 1.  The second set
# will be group 2. By passing the integer 1 or 2 to the group() match object method
# you can grab different parts of the matched text.  Passing 0 or nothing to
# the group() method will return the entire matched text.

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))

# If you would like to retrieve all the groups at once, use the groups() method

print(mo.groups())

# You can use mutliple assignment to assign these values variables

areaCode, mainNumber, mainNumberAnd = mo.groups()
print(areaCode)
print(mainNumber)

# Parens have a special meaning in regular expressions, but what do you
# do if you need to match a parenthesis in your text? For instance, maybe
# the phone numbers you are trying to match have the area code set in
# parentheses. In this case, you need to escape the ( and ) characters
# with a backslash. 


newPhoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d)-(\d\d\d\d)')
moGroups = newPhoneNumRegex.search('My phone number is (415)-555-4242')
print(moGroups.group(1))
print(moGroups.group(2))