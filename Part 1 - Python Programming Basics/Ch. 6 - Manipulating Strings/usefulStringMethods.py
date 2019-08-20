# The upper() and lower() string methods return a new string where all the letters in the original string have been converted
# to uppercase or lowercase, respectively.  These methods do not change the string itself but return new string values.

spam = 'Hello world!'
spam = spam.upper()
print(spam)

spam = spam.lower()
print(spam)

print("How are you?")
feeling = input()
if feeling.lower() == 'great':
    print('Ya know, I feel great too')
else:
    print('I hope the rest of your day is good!')

# The isupper() and islower() methods will return a Boolean True value if the string has at least one letter
# and all the letters are uppercase or lowercase, respectively.  Otherwise, the method returns False.

print('HELLO'.lower().islower())

# Along with islower() and isupper(), there are several string methods that have names beginning with the word is.
# These methods return a Boolean value that describes the nature of the string.  Here are some common isX
# string methods.
#
# isalpha() returns True if the string consists only of letters and is not blank
# isalnum() returns True if the string consists only of letters and numbers and is not blank.
# isdecimal() returns True if the string consists only of spaces, tabs, and new-lines and is not blank.
# istitle() returns True if the string consists only of words that began with an uppercase letter followed by
# only lowercase letters

# These string methods are useful when you need to validate user input
