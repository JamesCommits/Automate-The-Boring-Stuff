# The following program repeatedly asks users for their age and a password until they provide a valid input.
while True:
    age = input("Enter the SECRET age:     ")
    if age.isdecimal():
        break
    print("Please, we need numbers here.")

while True:
    secretPassword = input("Select a new password (letters and numbers only!):      ")
    if secretPassword.isalnum():
        break
    print('What did I just say? Passwords can only have numbers and letters! Try again.')