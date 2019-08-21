# The strip() string method will return a new string without any whitespace 
# characters at the beginning or end.  The lstrip() and rstrip() methods
# will remove whitespace characters from the left and right ends.  

spam = '     Hello World        '
spam.strip()
# 'Hello World'

spam.lstrip()
# 'Hello World       '

spam.rstrip()
# '       Hello World'


# Optionally, a string argument will specify which characters on the ends should be stripped.

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
# 'BaconSpamEggs'

# Passing strip() the argument 'ampS' will tell it to strip occurrences of a, m, p,
# and capital S from the ends of the string stored in spam. The order of the
# characters does not matter: strip('ampS') will do the same thing as 
# strip('mapS') or strip('Spam')