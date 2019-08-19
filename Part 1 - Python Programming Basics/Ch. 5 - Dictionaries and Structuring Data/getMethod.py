picnicItems = {'apples' : 5, 'cups' : 2}

# It's tedious to check whether a key exists in a dictionary before accessing that key's value.  
# Fortunately, dictionaries have a get() method that takes two arguments: the key of the value
# to retrieve and a fallback value to return if that key does not exist
print("I am bringing {} cups".format(str(picnicItems.get('cups', 0))))

# Because there is no 'eggs' key in the picnicItems dictionary, the default value 0 is returned by the get()
# method.  Without using get(), the code would have caused an error message.
print("I am bringing {} eggs".format(str(picnicItems.get('eggs', 0))))