# Short program that counts the number of occurrences of each letter in a string
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

# This program loops over each character in the 'message' variable's string, counting how often
# each character appears.  The setdefault() method call ensures that the key is in the count dictionary
# (with a default value of 0) so the program doesn't throw a KeyError error when count[character] = count[character] + 1
# is executed.