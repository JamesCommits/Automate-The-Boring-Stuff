# The rjust() and ljust() string methods return a padded version of the string
# they are called on, with spaces inserted to justify the text.  The first argument
# to both methods is an integer length for the justified string.

print('Hello'.rjust(10))
#      Hello
print('Hello'.rjust(20))
#               Hello
print('Hello'.ljust(10))
#'Hello          '

# 'Hello'.rjust(10) says that we want to right-justify 'Hello' in a string of
# total length 10.  'Hello' is five characters, so five spaces will be added 
# to it's left, giving us a string of 10 characters with 'Hello' 
# justified right

# An optional second argument to rjust() and ljust() will specify a fill
# character other than a space character.

print('Hello'.rjust(20, '*'))
# ***************Hello
print('Hello'.ljust(20, '-'))
# Hello---------------

# The center() string method works the same way but centers the string instead.

print('Hello'.center(20))
# '       Hello       '
print('Hello'.center(20, '='))
# =======Hello========

