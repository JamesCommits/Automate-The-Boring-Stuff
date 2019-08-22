# A Regex object's search() method searches the string it is passed for
# any matches to the regex.  The search() method will return 'None' if 
# the regex pattern is not found in the string. If the pattern IS found
# the search() method returns a Match object.  Match objects have a 
# group() method that will return the actual matched text from
# the searched string.  

import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: {}'.format(mo.group()))

# The mo variable name is just a generic name to use for Match objects.
# This example might seem complicated at first, but it is much shorter
# than our earlier version we made.

# Here we pass our desired pattern to re.compile() and store the 
# resulting Regex object in phoneNumRegex. Then we call search()
# on phoneNumRegex and pass search() the string we want to search
# for a match.  The result of the search gets stored in the variable
# 'mo'.  In this example, we know that our pattern will be found in
# the string so we know that a Match object will be returned.  
# Knowing that 'mo' contains a Match object and not the null value
# None, we can call group() on 'mo' to return the match.