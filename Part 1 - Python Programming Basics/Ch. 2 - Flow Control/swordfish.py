# This program will ask for a name and password.
while True:
    print('Who are you?')
    name = input()
    if name != 'James':
        continue
    print('Hello, {}.  Please enter the Password (It\'s a fish)'.format(name))
    password = input()
    if password != 'swordfish':
        break

print('Access Granted.')