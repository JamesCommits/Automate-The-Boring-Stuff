# The join() method is useful when you have a list of strings that need to be joined together
# into a single string value.  The join() method is called on a string, gets passed a list
# of strings, and returns a string.  

print(', ').join(['cats', 'rats', 'bats'])
# result = 'cats, rats, bats'

# Notice that the string join() calls on is inserted between each string of the list argument.

# Remember that join() is called on a string value and is passed a list value.  
# The split() method does the opposite: It's called on a string value and returns a list
# of strings. 

print('My name is James'.split())
# result = ['My', 'name', 'is', 'James']

# By default, the string 'My name is James' is split wherever whitespace characters such as
# the space, tab, or newline characters are found.  These whitespace characters are not
# included in the strings in the returned list.  You can pass a delimeter string to the
# split() method to specify a different string to split upon. For example:

print('MyABCnameABCisABCJames').split('ABC')
# result = ['My', 'name', 'is', 'James']

