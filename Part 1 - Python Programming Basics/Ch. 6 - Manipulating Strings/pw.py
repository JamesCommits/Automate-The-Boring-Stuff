#! python3
# An insecure password locker project.

PASSWORDS = {'email' : 'F3fdf9r1fg39d', 'blog' : '4tgf233rgsg354FS', 'luggage' : '12345'}


import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()


account = sys.argv[1]  # first command line arg is the account name
