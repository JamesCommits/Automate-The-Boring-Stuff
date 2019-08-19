# Multiple assingment lets you assign multiple variables with the values in a list in one line of code
# So instead of the below code:
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

# You could type that same code this way
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat

# The number of variables and the length of the list must be exactly equal, or you'll get a ValueError

