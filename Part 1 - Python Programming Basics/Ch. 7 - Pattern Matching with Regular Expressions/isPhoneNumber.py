def isPhoneNumber(text):
    # First the function checks to see if the string is 12 characters long
    if len(text) != 12:
        return False
    # Then it checks to make sure that the area code only consists of numbers
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    # The number must have the first hyphen after the area code
    if text[3] != '-':
        return False
    # Checks for three more numbers
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    # Checks for another hyphen to be present
    if text[7] != '-':
        return False
    # And then finally for the last four numbers of the phone number
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    # If the program makes it past all the checks, it's returned true.
    return True

# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi Moshi is a phone number:')
# print(isPhoneNumber('Moshi Moshi'))

message = 'Call me at 415-555-1011 tomorrow.  415-555-9999 is my office.'
for i in range(len(message)):
    # On each iteration of the for loop, a new chunk of 12 characters from message
    # is assigned to the variable chunk.  For example, on the first iteration, i is 0
    # and chunk is assigned message[0:12] (that is, the string 'Call me at 4').  On
    # the next iteration, i is 1, and chunk is assigned message[1:13](the string 'all me at 41')
    chunk = message[i:i+12]
    # You pass chunk to isPhoneNumber() to see whether it matches the phone number
    # pattern, and if so, you print the chunk
    if isPhoneNumber(chunk):
        print('Phone number found: {}'.format(chunk))
print('Done!')