# You'll often have to set a value in a dictionary for a certain key only if that key does not already
# have a value.

# The setdefault() method offers a way to do this in one line of code.  The first argument passed to
# method is they key to check for, and the second argument is the value to set at that key
# if they key does not exist.  If the key does exist, the setdefault() method returns the
# key's value.

spam = {'name' : 'Pooka', 'age' : 5}
spam.setdefault('color', 'black')
print(spam)

# If we were to call the setdefault() method again with the color white.  The color in the dictionary
# would remain unchanged because it already has an existing key named color.