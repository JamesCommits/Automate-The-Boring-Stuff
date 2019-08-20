# Strings use indexes and slices the same way lists do.  You can think of the string 'Hello World!' as a list 
# and each character in the string as an item with a corresponding index. The spaces and exclamation point
# are included in the character count, so 'Hello World!' is 12 characters long, from 'H' at index 0
# to '!' at index 11

spam = 'Hello World!'
print(spam[0])
print(spam[4])
print(spam[-1])

print(spam[:5])
# The print syntax above will include everything from index 0-4 leaving out 5

print(spam[6:])
# The print syntax above will include everything from index 6-11 leaving out 6

