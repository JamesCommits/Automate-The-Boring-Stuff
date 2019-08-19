# When you assign a list to a variable, you are actually assigning a list reference
# to the variable.  A reference is a value that points to some bit of data,
# and a list reference is a value that points to a list.
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
