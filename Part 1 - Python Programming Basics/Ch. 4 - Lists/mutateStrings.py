name = 'Zophie a cat'

# Here we use [0:7] and [8:12] to identify characters we don't want to replace
# Notice the 'name' string is still intact because strings are immutable
newName = name[0:7] + ' the ' + name[8:12]
print(name)
print(newName)